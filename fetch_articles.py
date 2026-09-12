import requests
from bs4 import BeautifulSoup
import urllib.parse
import re
import os
import time

BASE_URL = 'https://www.rankia.com'
AUTHOR_URL = f'{BASE_URL}/usuarios/francisco-llinares/articulos'

def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    return resp.text

def extract_article_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    # Find all article links; they are within <article> tags or <a> with href containing /articulos/
    for a in soup.select('a[href*="/articulos/"]'):
        href = a.get('href')
        if href:
            full_url = urllib.parse.urljoin(BASE_URL, href)
            # Avoid duplicates
            if full_url not in links:
                links.append(full_url)
    # Also maybe there are pagination links; we'll handle later
    return links

def get_article_details(url):
    html = get_page(url)
    soup = BeautifulSoup(html, 'html.parser')
    # Title: look for h1 or og:title or title tag
    title_tag = soup.find('h1')
    if title_tag:
        title = title_tag.get_text(strip=True)
    else:
        og_title = soup.find('meta', property='og:title')
        if og_title:
            title = og_title.get('content', '').strip()
        else:
            title_tag = soup.find('title')
            title = title_tag.get_text(strip=True) if title_tag else 'Untitled'
    # Remove site suffix if present
    title = re.sub(r'\s*[-|]\s*Rankia.*$', '', title)
    # Date: look for time[datetime] or meta article:published_time
    date = None
    time_tag = soup.find('time', attrs={'datetime': True})
    if time_tag:
        date = time_tag['datetime']
        if 'T' in date:
            date = date.split('T')[0]
    else:
        meta_date = soup.find('meta', property='article:published_time')
        if meta_date:
            date = meta_date.get('content')
            if 'T' in date:
                date = date.split('T')[0]
        else:
            # Look for any element with class containing date
            date_el = soup.find(class_=re.compile(r'date|time|published', re.I))
            if date_el:
                date_text = date_el.get_text(strip=True)
                # Try to extract YYYY-MM-DD
                match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_text)
                if match:
                    date = f'{match.group(1)}-{match.group(2)}-{match.group(3)}'
    if not date:
        date = 'unknown'
    # Content: try to get main article content
    content = ''
    # Try common selectors
    for selector in ['article', '.content', '.post-content', '.entry-content', '.article-body']:
        el = soup.select_one(selector)
        if el:
            # Remove scripts and styles
            for script in el(['script', 'style']):
                script.decompose()
            content = el.get_text(separator='\n', strip=True)
            break
    if not content:
        # fallback: get all text
        for script in soup(['script', 'style']):
            script.decompose()
        content = soup.get_text(separator='\n', strip=True)
    return {
        'url': url,
        'title': title,
        'date': date,
        'content': content
    }

def sanitize_filename(title):
    # Remove invalid characters for filename
    title = re.sub(r'[<>:"/\\|?*\x00-\x1F]', '', title)
    title = title.strip()
    # Replace spaces with underscores? We'll keep spaces but replace with _ for safety
    title = title.replace(' ', '_')
    # Limit length
    if len(title) > 100:
        title = title[:100]
    return title

def main():
    print('Fetching author page...')
    html = get_page(AUTHOR_URL)
    links = extract_article_links(html)
    print(f'Found {len(links)} article links')
    # Limit to first 5 for testing? We'll process all.
    os.makedirs('articles', exist_ok=True)
    for i, link in enumerate(links, start=1):
        print(f'Processing {i}/{len(links)}: {link}')
        try:
            details = get_article_details(link)
            date = details['date']
            title = details['title']
            content = details['content']
            if date == 'unknown':
                # Try to extract date from URL maybe
                # Skip? We'll use unknown
                pass
            safe_title = sanitize_filename(title)
            filename = f'{date}_{safe_title}.md' if date != 'unknown' else f'{safe_title}.md'
            filepath = os.path.join('articles', filename)
            # Write markdown
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f'---\n')
                f.write(f'title: \"{title}\"\n')
                f.write(f'date: {date}\n')
                f.write(f'source: {link}\n')
                f.write(f'---\n\n')
                f.write(content)
            print(f'  Saved to {filename}')
            time.sleep(1)  # be polite
        except Exception as e:
            print(f'  Error processing {link}: {e}')
    print('Done.')

if __name__ == '__main__':
    main()
