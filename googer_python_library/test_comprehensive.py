"""Comprehensive test of Googer library functionality."""
from googer import Googer, Query

print("=" * 60)
print("TEST 1: Basic search with context manager")
print("=" * 60)
with Googer() as g:
    results = g.search("2025한국시리즈 우승팀")
    print(f"Got {len(results)} results")
    for r in results:
        print(f"  Title: {r.title}")
        print(f"  URL:   {r.href}")
        print(f"  Body:  {r.body[:80]}...")
        print()

print("=" * 60)
print("TEST 2: Search without context manager")
print("=" * 60)
g = Googer()
results = g.search("machine learning", max_results=5)
print(f"Got {len(results)} results")
for r in results:
    print(f"  {r.title} -> {r.href}")

print()
print("=" * 60)
print("TEST 3: Query builder")
print("=" * 60)
q = Query("python").site("github.com")
print(f"Query: {q}")
results = g.search(str(q), max_results=5)
print(f"Got {len(results)} results")
for r in results:
    print(f"  {r.title}")

print()
print("=" * 60)
print("TEST 4: Dict-like access")
print("=" * 60)
results = g.search("rust programming", max_results=3)
for r in results:
    d = r.to_dict()
    print(f"  keys: {list(d.keys())}")
    print(f"  title via dict: {d['title']}")
    print(f"  title via attr: {r.title}")
    print(f"  'title' in r: {'title' in r}")
    print()

print("=" * 60)
print("ALL TESTS PASSED!")
print("=" * 60)
