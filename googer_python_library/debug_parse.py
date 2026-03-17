"""Parse the saved GSA HTML with the same selectors the Rust code uses."""
try:
    from bs4 import BeautifulSoup
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'beautifulsoup4', '-q'])
    from bs4 import BeautifulSoup

# Use lxml-like CSS selectors via BeautifulSoup to emulate what scraper crate does
with open('debug_gsa.html', 'r', encoding='utf-8') as f:
    html = f.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Current selectors from config.rs
TEXT_ITEMS_SELECTOR = "div[data-snc]"
TEXT_TITLE_SELECTOR = "div[role='link']"
TEXT_HREF_SELECTOR = "a[href]"
TEXT_BODY_SELECTOR = "div[data-sncf]"

items = soup.select(TEXT_ITEMS_SELECTOR)
print(f"Found {len(items)} data-snc items\n")

for i, item in enumerate(items):
    title_el = item.select_one(TEXT_TITLE_SELECTOR)
    href_el = item.select_one(TEXT_HREF_SELECTOR)
    body_el = item.select_one(TEXT_BODY_SELECTOR)

    title = title_el.get_text(strip=True) if title_el else "(no title)"
    href = href_el.get('href', '(no href)') if href_el else "(no href)"
    body = body_el.get_text(strip=True) if body_el else "(no body)"

    # Clean URL
    if href.startswith('/url?q='):
        href = href.split('/url?q=')[1].split('&')[0]

    print(f"--- Result {i+1} ---")
    print(f"Title: {title[:100]}")
    print(f"Href: {href[:100]}")
    print(f"Body: {body[:150]}")
    print()
