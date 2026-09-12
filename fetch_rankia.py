import requests
import re
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
import os
import time

BASE_URL = 'https://www.rankia.com'
AUTHOR_URL = f'{BASE_URL}/usuarios/francisco-llinares/articulos'

class SimpleHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.in_title = False
        self.title = []
        self.in_content = False
        self.content = []
        self.date = None
        self.current_tag = ''
    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        if tag == 'a':
            for attr, val in attrs:
                if attr == 'href' and val and '/articulos/' in val:
                    self.links.append(urljoin(BASE_URL, val))
        if tag == 'h1':
            self.in_title = True
        # Look for time[datetime] or meta article:published_time
        if tag == 'time':
            for attr, val in attrs:
                if attr == 'datetime':
                    self.date = val.split('T')[0] if val else None
        if tag == 'meta':
            attrs_dict = dict(attrs)
            if attrs_dict.get('property') == 'article:published_time':
                content = attrs_dict.get('content')
                if content:
                    self.date = content.split('T')[0] if content else None
    def handle_endtag(self, tag):
        if tag == 'h1':
            self.in_title = False
        # content detection: we'll just collect all text for simplicity
    def handle_data(self, data):
        if self.in_title:
            self.title.append(data.strip())
        # For simplicity, we'll capture all text later via regex

def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'
    }
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f'Error fetching {url}: {e}')
        return None

def extract_article_links(html):
    parser = SimpleHTMLParser()
    parser.feed(html)
    # deduplicate
    return list(set(parser.links))

def extract_article_details(html, url):
    # Use regex to extract title, date, content
    title = None
    date = None
    # Try to find <h1>...</h1>
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.IGNORECASE | re.DOTALL)
    if h1_match:
        title = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
    else:
        # fallback to title tag
        title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
        if title_match:
            title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
            # Remove site suffix
            title = re.sub(r'\s*[-|]\s*Rankia.*$', '', title)
    # Date: look for time[datetime] or meta
    date_match = re.search(r'<time[^>]*datetime=["\']([^"\']+)', html, re.IGNORECASE)
    if date_match:
        date = date_match.group(1).split('T')[0]
    else:
        meta_match = re.search(r'<meta[^>]*property=["\']article:published_time["\'][^>]*content=["\']([^"\']+)', html, re.IGNORECASE)
        if meta_match:
            date = meta_match.group(1).split('T')[0]
    # If still not found, look for any date pattern in text
    if not date:
        # Search for YYYY-MM-DD in the first 5000 chars
        match = re.search(r'(\d{4})-(\d{2})-(\d{2})', html[:5000])
        if match:
            date = f'{match.group(1)}-{match.group(2)}-{match.group(3)}'
    # Content: try to get main article content
    # Look for common containers
    content = ''
    # Try to find <article> or div with class containing content
    # We'll do a simple extraction: get all text and clean
    # Remove script and style tags
    cleaned = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html, flags=re.DOTALL | re.IGNORECASE)
    # Extract text from body
    body_match = re.search(r'<body[^>]*>(.*?)</body>', cleaned, re.IGNORECASE | re.DOTALL)
    if body_match:
        body = body_match.group(1)
        # Remove all tags
        body = re.sub(r'<[^>]+>', ' ', body)
        # Clean whitespace
        body = re.sub(r'\s+', ' ', body).strip()
        content = body
    else:
        # fallback: get all text from html after removing tags
        cleaned2 = re.sub(r'<[^>]+>', ' ', html)
        content = re.sub(r'\s+', ' ', cleaned2).strip()
    return {
        'url': url,
        'title': title if title else 'Untitled',
        'date': date if date else 'unknown',
        'content': content
    }

def sanitize_filename(title):
    # Remove invalid characters
    title = re.sub(r'[<>:"/\\|?*\x00-\x1F]', '', title)
    title = title.strip()
    title = title.replace(' ', '_')
    if not title:
        title = 'article'
    # Limit length
    if len(title) > 100:
        title = title[:100]
    return title

def main():
    print(f'Fetching author page: {AUTHOR_URL}')
    html = get_page(AUTHOR_URL)
    if not html:
        print('Failed to fetch author page')
        return
    links = extract_article_links(html)
    print(f'Found {len(links)} unique article links')
    # Limit to first 10 for testing? We'll process all but break after 10 for now.
    max_articles = 20
    if len(links) > max_articles:
        print(f'Limiting to first {max_articles} articles for testing')
        links = links[:max_articles]
    os.makedirs('articles', exist_ok=True)
    for i, link in enumerate(links, start=1):
        print(f'[{i}/{len(links)}] Processing: {link}')
        article_html = get_page(link)
        if not article_html:
            print('  Failed to fetch article')
            continue
        details = extract_article_details(article_html, link)
        print(f'  Title: {details["title"][:60]}...')
        print(f'  Date: {details["date"]}')
        safe_title = sanitize_filename(details['title'])
        if details['date'] != 'unknown':
            filename = f'{details["date"]}_{safe_title}.md'
        else:
            filename = f'{safe_title}.md'
        filepath = os.path.join('articles', filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f'---\n')
            f.write(f'title: "{details["title"]}"\n')
            f.write(f'date: {details["date"]}\n')
            f.write(f'source: {details["url"]}\n')
            f.write(f'---\n\n')
            f.write(details['content'])
        print(f'  Saved to {filename}')
        time.sleep(1)  # be polite
    print('Done.')

if __name__ == '__main__':
    main()
