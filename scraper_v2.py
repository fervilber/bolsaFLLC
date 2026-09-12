#!/usr/bin/env python3
"""Scraper v2: extrae el contenido COMPLETO de cada artículo del blog de Francisco Llinares.
Corrige el problema de la v1 que no extraía todo el texto del trix-content."""

import requests, re, os, sys, json, time
from pathlib import Path
from collections import Counter

GOOGLEBOT_UA = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
OUTPUT = Path('/home/vilber/proyectos/rankia-francisco-llinares/articles')
URLS_FILE = Path('/home/vilber/proyectos/rankia-francisco-llinares/article_urls.json')

OUTPUT.mkdir(parents=True, exist_ok=True)
session = requests.Session()
session.headers.update({'User-Agent': GOOGLEBOT_UA})


def extract_full_content(html):
    """Extrae el contenido completo del artículo desde rnk-BlogPost_Content.
    Maneja tanto el formato antiguo (<p> directo) como el reciente (trix-content)."""
    # Find the article body: <div class="rnk-BlogPost_Content"> ... </div> before rnk-BlogPost_Sticky
    m = re.search(
        r'<div class="rnk-BlogPost_Content">(.*?)</div>\s*<div class="rnk-BlogPost_Sticky"',
        html, re.DOTALL
    )
    if not m:
        # Fallback: get from rnk-BlogPost_Content to </article>
        m = re.search(r'<div class="rnk-BlogPost_Content">(.*?)</article>', html, re.DOTALL)
    
    if not m:
        return ''
    
    content_html = m.group(1)
    
    # Process:
    # Convert <br><br> to paragraph breaks
    content_html = re.sub(r'<br\s*/?>\s*<br\s*/?>', '\n\n', content_html, flags=re.IGNORECASE)
    # Convert single <br> to newline
    content_html = re.sub(r'<br\s*/?>', '\n', content_html, flags=re.IGNORECASE)
    # Add newlines after block-level closes
    for tag in ['</div>', '</blockquote>', '</p>', '</h1>', '</h2>', '</h3>', '</h4>', '</li>']:
        content_html = content_html.replace(tag, tag + '\n')
    # Remove script/style/svg
    content_html = re.sub(r'<(script|style|svg)[^>]*>.*?</\1>', '', content_html, flags=re.DOTALL | re.IGNORECASE)
    # Remove all tags
    content_html = re.sub(r'<[^>]+>', '', content_html)
    # Decode entities
    content_html = content_html.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    content_html = content_html.replace('&quot;', '"').replace('&#039;', "'").replace('&nbsp;', ' ')
    # Clean whitespace
    content_html = re.sub(r'\n{3,}', '\n\n', content_html)
    content_html = re.sub(r'[ \t]+', ' ', content_html)
    content_html = '\n'.join(line.strip() for line in content_html.split('\n'))
    
    # Remove trailing noise (vote counts, share buttons, etc.)
    lines = content_html.split('\n')
    cleaned = []
    for i, line in enumerate(lines):
        s = line.strip()
        # Skip standalone vote counts (numbers like "9", "8", "15 12")
        if re.match(r'^\d+(\s+\d+)?$', s) and len(s) < 10:
            prev_short = i > 0 and len(lines[i-1].strip()) < 80
            next_short = i >= len(lines)-1 or len(lines[i+1].strip()) < 80
            if prev_short or next_short:
                continue
        # Skip UI noise
        if s in ['Responder', 'Seguir', 'Compartir en']:
            continue
        if s.startswith('Compartir en ') or s.startswith('¿Quieres aprender'):
            continue
        if s.startswith('Para navegar sin cookies') or s.startswith('inicia sesión'):
            continue
        cleaned.append(line)
    
    # Remove trailing empty lines and vote numbers
    while cleaned and (not cleaned[-1].strip() or re.match(r'^\d+$', cleaned[-1].strip())):
        cleaned.pop()
    
    return '\n'.join(cleaned).strip()


def fetch_and_extract(url):
    """Descarga un artículo y extrae título, fecha y contenido completo."""
    try:
        resp = session.get(url, timeout=15)
        resp.raise_for_status()
    except Exception as e:
        raise e
    
    html = resp.text
    
    # Title
    title = ''
    m = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL | re.IGNORECASE)
    if m:
        title = re.sub(r'<[^>]+>', '', m.group(1)).strip()
    
    # Date
    date = ''
    m = re.search(r'<time[^>]*datetime=["\']([^"\']+)', html, re.IGNORECASE)
    if m:
        date = m.group(1).split('T')[0]
    if not date:
        m = re.search(r'article:published_time["\'][^>]*content=["\']([^"\']+)', html, re.IGNORECASE)
        if m:
            date = m.group(1).split('T')[0]
    
    # Content
    content = extract_full_content(html)
    
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


def main():
    with open(URLS_FILE) as f:
        urls = json.load(f)
    
    print(f"📥 Re-descargando {len(urls)} artículos con extractor mejorado...")
    
    success = 0
    errors = 0
    total_chars = 0
    
    for i, url in enumerate(urls, 1):
        try:
            article = fetch_and_extract(url)
            save_article(article)
            success += 1
            total_chars += len(article['content'])
            
            if i % 50 == 0 or i == 1:
                avg = total_chars // success if success > 0 else 0
                print(f"  [{i}/{len(urls)}] {success} OK, {errors} err | avg={avg} chars | last: {len(article['content'])} chars - {article['title'][:60]}")
        except Exception as e:
            errors += 1
            if errors <= 3:
                print(f"  ❌ [{i}] {url}: {e}")
        
        time.sleep(0.3)
    
    print(f"\n✅ Completado: {success} OK, {errors} errores")
    print(f"   Total chars: {total_chars:,} | Avg: {total_chars//success if success else 0} chars")

    # Stats
    files = list(OUTPUT.glob('*.md'))
    total_size = sum(f.stat().st_size for f in files)
    print(f"   Archivos: {len(files)} | Tamaño total: {total_size/1024/1024:.1f} MB")
    
    # Content length distribution
    lengths = []
    for f in files:
        text = f.read_text(encoding='utf-8')
        # Count content after frontmatter
        parts = text.split('---\n', 2)
        if len(parts) >= 3:
            lengths.append(len(parts[2]))
    
    if lengths:
        print(f"   Contenido: min={min(lengths)}, max={max(lengths)}, mediana={sorted(lengths)[len(lengths)//2]}")
        short = sum(1 for l in lengths if l < 200)
        print(f"   Artículos con <200 chars: {short}/{len(lengths)}")


if __name__ == '__main__':
    main()