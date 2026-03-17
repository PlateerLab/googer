import urllib.request
import re

# Test with GSA user agent (what the library uses)
gsa_ua = "Mozilla/5.0 (iPhone; CPU iPhone OS 18_7_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/411.0.879111500 Mobile/15E148 Safari/604.1"

req = urllib.request.Request(
    'https://www.google.com/search?q=python+programming&start=0&hl=en&lr=lang_en',
    headers={'User-Agent': gsa_ua}
)
r = urllib.request.urlopen(req)
html_gsa = r.read().decode('utf-8')
print(f"=== GSA UA HTML length: {len(html_gsa)} ===")
with open('debug_gsa.html', 'w', encoding='utf-8') as f:
    f.write(html_gsa)

# Test with Chrome desktop UA
chrome_ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

req2 = urllib.request.Request(
    'https://www.google.com/search?q=python+programming&start=0&hl=en&lr=lang_en',
    headers={'User-Agent': chrome_ua}
)
r2 = urllib.request.urlopen(req2)
html_chrome = r2.read().decode('utf-8')
print(f"=== Chrome UA HTML length: {len(html_chrome)} ===")
with open('debug_chrome.html', 'w', encoding='utf-8') as f:
    f.write(html_chrome)

# Look for patterns in GSA HTML
print("\n--- GSA HTML patterns ---")
for pattern in ['data-snc', 'data-sncf', 'data-sokoban', 'class="g"', 'class="Gx5Zad"',
                'role="link"', '/url?q=', 'class="BNeawe"', 'class="kCrYT"',
                'class="ZINbbc"', 'class="tF2Cxc"', 'class="yuRUbf"', 'class="VwiC3b"',
                'class="egMi0 kCrYT"', 'class="BVG0Nb"', 'data-hveid']:
    count = html_gsa.count(pattern)
    if count > 0:
        print(f"  {pattern}: {count} occurrences")

print("\n--- Chrome HTML patterns ---")
for pattern in ['data-snc', 'data-sncf', 'data-sokoban', 'class="g"', 'class="Gx5Zad"',
                'role="link"', '/url?q=', 'class="BNeawe"', 'class="kCrYT"',
                'class="ZINbbc"', 'class="tF2Cxc"', 'class="yuRUbf"', 'class="VwiC3b"',
                'class="egMi0 kCrYT"', 'class="BVG0Nb"', 'data-hveid']:
    count = html_chrome.count(pattern)
    if count > 0:
        print(f"  {pattern}: {count} occurrences")

# Check for redirect/consent pages
print("\n--- Consent/redirect check ---")
print(f"GSA consent: {'consent' in html_gsa.lower()}")
print(f"Chrome consent: {'consent' in html_chrome.lower()}")
print(f"GSA captcha: {'captcha' in html_gsa.lower()}")
print(f"Chrome captcha: {'captcha' in html_chrome.lower()}")
