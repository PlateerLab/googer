from html.parser import HTMLParser
import re

class SelectorChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data_snc_count = 0
        self.data_snc_tags = []
        self.data_sncf_count = 0
        self.data_sncf_tags = []
        self.role_link_count = 0
        self.role_link_tags = []
        self.url_q_count = 0
        self.current_snc_item = None
        self.in_snc = False
        self.snc_items = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if 'data-snc' in attr_dict:
            self.data_snc_count += 1
            self.data_snc_tags.append((tag, attr_dict.get('data-snc', '')))
        if 'data-sncf' in attr_dict:
            self.data_sncf_count += 1
            self.data_sncf_tags.append((tag, attr_dict.get('data-sncf', '')))
        if attr_dict.get('role') == 'link':
            self.role_link_count += 1
            self.role_link_tags.append(tag)
        href = attr_dict.get('href', '')
        if '/url?q=' in href:
            self.url_q_count += 1

with open('debug_gsa.html', 'r', encoding='utf-8') as f:
    html = f.read()

checker = SelectorChecker()
checker.feed(html)

print(f"data-snc elements: {checker.data_snc_count}")
for tag, val in checker.data_snc_tags[:5]:
    print(f"  <{tag} data-snc=\"{val}\">")

print(f"\ndata-sncf elements: {checker.data_sncf_count}")
for tag, val in checker.data_sncf_tags[:5]:
    print(f"  <{tag} data-sncf=\"{val}\">")

print(f"\nrole='link' elements: {checker.role_link_count}")
for tag in checker.role_link_tags[:5]:
    print(f"  <{tag}>")

print(f"\n/url?q= links: {checker.url_q_count}")

# Let me try to extract a sample data-snc block with context
import re

# Find first data-snc block with surrounding content
snc_pattern = re.compile(r'<div[^>]*data-snc[^>]*>.*?</div>', re.DOTALL)
matches = snc_pattern.findall(html)
print(f"\n=== First data-snc block (first 2000 chars) ===")
if matches:
    block = matches[0][:2000]
    print(block)

# Find context around data-snc more broadly
idx = html.find('data-snc')
if idx >= 0:
    start = max(0, idx - 200)
    end = min(len(html), idx + 2000)
    snippet = html[start:end]
    print(f"\n=== Context around first data-snc (chars {start}-{end}) ===")
    print(snippet[:3000])
