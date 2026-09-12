#!/usr/bin/env python3
"""Scraper para el blog de Francisco Llinares Coloma en Rankia.
Fase 1: Recopila todas las URLs de artículos desde el RSS + paginación del blog.
Fase 2: Descarga cada artículo y lo guarda como Markdown.
"""

import requests
import re
import os
import sys
import time
import json
from datetime import datetime
from pathlib import Path

GOOGLEBOT_UA = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
BASE = 'https://www.rankia.com'
BLOG = f'{BASE}/blog/llinares'
RSS = f'{BASE}/blogs/llinares/feed'
OUTPUT = Path('/home/vilber/proyectos/rankia-francisco-llinares/articles')
URLS_FILE = Path('/home/vilber/proyectos/rankia-francisco-llinares/article_urls.json')

OUTPUT.mkdir(parents=True, exist_ok=True)

session = requests.Session()
session.headers.update({'User-Agent': GOOGLEBOT_UA})


# ── FASE 1: Recopilar URLs ──────────────────────────────────────────

def collect_rss_urls():
    """Extrae URLs del feed RSS."""
    urls = set()
    try:
        resp = session.get(RSS, timeout=15)
        resp.raise_for_status()
        links = re.findall(r'<link>(https://www\.rankia\.com/blog/llinares/\d+[^<]*)</link>', resp.text)
        urls.update(links)
        print(f"  RSS: {len(links)} artículos")
    except Exception as e:
        print(f"  RSS error: {e}")
    return urls


def collect_page_urls(page_num):
    """Extrae URLs de una página del blog."""
    url = f'{BLOG}?page={page_num}' if page_num > 1 else BLOG
    try:
        resp = session.get(url, timeout=15)
        resp.raise_for_status()
        links = re.findall(r'href="(/blog/llinares/\d+[^"]*)"', resp.text)
        urls = {f'{BASE}{l}' for l in links}
        print(f"  Página {page_num}: {len(urls)} artículos")
        return urls
    except Exception as e:
        print(f"  Página {page_num} error: {e}")
        return set()


def discover_pages():
    """Descubre el número total de páginas del blog."""
    try:
        resp = session.get(BLOG, timeout=15)
        resp.raise_for_status()
        pages = set()
        for m in re.finditer(r'page=(\d+)', resp.text):
            pages.add(int(m.group(1)))
        max_page = max(pages) if pages else 1
        print(f"  Páginas descubiertas: hasta la {max_page}")
        return max_page
    except Exception as e:
        print(f"  Error descubriendo páginas: {e}")
        return 1


def collect_all_urls():
    """Recopila todas las URLs de artículos y las guarda."""
    print("\n📋 FASE 1: Recopilando URLs...")
    
    all_urls = set()
    
    # RSS feed
    all_urls.update(collect_rss_urls())
    
    # Blog pagination
    max_page = discover_pages()
    
    for page in range(1, max_page + 1):
        urls = collect_page_urls(page)
        all_urls.update(urls)
        if page % 10 == 0:
            print(f"  → Acumulado: {len(all_urls)} URLs únicas")
        time.sleep(0.3)  # Be polite
    
    # Save URLs
    with open(URLS_FILE, 'w') as f:
        json.dump(sorted(all_urls), f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Total: {len(all_urls)} URLs únicas guardadas en {URLS_FILE}")
    return sorted(all_urls)


# ── FASE 2: Descargar artículos ─────────────────────────────────────

def fetch_article(url):
    """Descarga la página del artículo."""
    resp = session.get(url, timeout=15)
    resp.raise_for_status()
    return resp.text


def extract_article(html, url):
    """Extrae título, fecha y contenido del HTML."""
    title = ''
    m = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL | re.IGNORECASE)
    if m:
        title = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    
    date = ''
    m = re.search(r'<time[^>]*datetime=["\']([^"\']+)', html, re.IGNORECASE)
    if m:
        date = m.group(1).split('T')[0]
    if not date:
        m = re.search(r'article:published_time["\'][^>]*content=["\']([^"\']+)', html, re.IGNORECASE)
        if m:
            date = m.group(1).split('T')[0]
    
    # Extract trix-content
    content = ''
    m = re.search(
        r'<div[^>]*class="[^"]*trix-content[^"]*"[^>]*>(.*?)</div>\s*(?:</div>\s*</div>\s*<footer|'
        r'<div[^>]*class="[^"]*rnk-BlogPost_Author|'
        r'<div[^>]*class="[^"]*rnk-BlogPost_Comments)',
        html, re.DOTALL | re.IGNORECASE
    )
    if not m:
        m = re.search(
            r'<div[^>]*class="[^"]*trix-content[^"]*"[^>]*>(.*?)</article>',
            html, re.DOTALL | re.IGNORECASE
        )
    
    if m:
        raw = m.group(1)
        raw = re.sub(r'<(script|style|svg)[^>]*>.*?</\1>', '', raw, flags=re.DOTALL | re.IGNORECASE)
        raw = re.sub(r'<br\s*/?>\s*<br\s*/?>', '\n\n', raw, flags=re.IGNORECASE)
        raw = re.sub(r'<br\s*/?>', '\n', raw, flags=re.IGNORECASE)
        raw = re.sub(r'<[^>]+>', '', raw)
        raw = raw.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
        raw = raw.replace('&quot;', '"').replace('&#039;', "'").replace('&nbsp;', ' ')
        raw = re.sub(r'\n{3,}', '\n\n', raw)
        raw = re.sub(r'[ \t]+', ' ', raw)
        raw = '\n'.join(line.strip() for line in raw.split('\n'))
        content = raw.strip()
    
    return {'title': title, 'date': date, 'content': content, 'url': url}


def sanitize_filename(title, date):
    safe = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '', title)
    safe = safe.strip().replace(' ', '_')[:100]
    if not safe:
        safe = 'article'
    return f'{date}_{safe}.md' if date else f'{safe}.md'


def save_article(article):
    filename = sanitize_filename(article['title'], article['date'])
    filepath = OUTPUT / filename
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write(f'title: "{article["title"]}"\n')
        f.write(f'date: {article["date"]}\n')
        f.write(f'source: {article["url"]}\n')
        f.write('author: Francisco Llinares Coloma\n')
        f.write('blog: Rankia\n')
        f.write('---\n\n')
        f.write(f'# {article["title"]}\n\n')
        f.write(article['content'] if article['content'] else '_No se pudo extraer el contenido._')
    return filepath


def download_articles(urls, resume=True):
    """Descarga y guarda todos los artículos."""
    print(f"\n📥 FASE 2: Descargando {len(urls)} artículos...")
    
    # Resume support: skip already downloaded
    existing = set()
    if resume and OUTPUT.exists():
        for f in OUTPUT.glob('*.md'):
            existing.add(f.name)
    if existing:
        print(f"  {len(existing)} ya descargados, se omitirán")
    
    success = 0
    skipped = 0
    errors = 0
    
    for i, url in enumerate(urls, 1):
        # Quick check: does this URL's expected filename already exist?
        url_id = re.search(r'/llinares/(\d+)', url)
        already = False
        if url_id and resume:
            for f in existing:
                if url_id.group(1) in f:
                    already = True
                    skipped += 1
                    break
        if already:
            if i % 50 == 0:
                print(f"  [{i}/{len(urls)}] {skipped} omitidos, {success} OK, {errors} errores")
            continue
        
        try:
            html = fetch_article(url)
            article = extract_article(html, url)
            save_article(article)
            success += 1
        except Exception as e:
            errors += 1
            if errors <= 5:
                print(f"  ❌ Error {url}: {e}")
        
        if i % 20 == 0:
            print(f"  [{i}/{len(urls)}] {success} OK, {skipped} omitidos, {errors} errores")
        
        time.sleep(0.3)  # Rate limiting
    
    print(f"\n✅ Completado: {success} descargados, {skipped} omitidos, {errors} errores")
    return success, skipped, errors


# ── MAIN ─────────────────────────────────────────────────────────────

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--resume':
        # Skip collection, just download
        if URLS_FILE.exists():
            with open(URLS_FILE) as f:
                urls = json.load(f)
            print(f"📂 Cargadas {len(urls)} URLs desde {URLS_FILE}")
            download_articles(urls, resume=True)
        else:
            print(f"❌ No existe {URLS_FILE}. Ejecuta sin --resume primero.")
            sys.exit(1)
    else:
        urls = collect_all_urls()
        download_articles(urls, resume=True)
    
    # Summary
    count = len(list(OUTPUT.glob('*.md')))
    print(f"\n📊 Total archivos Markdown en {OUTPUT}: {count}")