import urllib.request

req = urllib.request.Request(
    'https://www.google.com/search?q=python+programming&start=0&hl=en&lr=lang_en&safe=active',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
)
r = urllib.request.urlopen(req)
html = r.read().decode('utf-8')
print(f"HTML length: {len(html)}")
print(f"data-snc: {'data-snc' in html}")
print(f"data-sncf: {'data-sncf' in html}")
class_g = 'class="g"'
print(f"class g: {class_g in html}")
print(f"div.MjjYud: {'MjjYud' in html}")
print(f"div.g.Ww4FFb: {'Ww4FFb' in html}")

with open('debug_google.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Saved to debug_google.html")
