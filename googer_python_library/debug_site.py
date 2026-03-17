"""Debug the site: operator issue."""
from googer import Googer, Query, NoResultsException

g = Googer()

# Test 1: plain query (should work)
try:
    results = g.search("python", max_results=3)
    print(f"Plain 'python': got {len(results)} results")
except NoResultsException as e:
    print(f"Plain 'python': NoResults - {e}")

# Test 2: site operator in query string
try:
    results = g.search("python site:github.com", max_results=5)
    print(f"'python site:github.com': got {len(results)} results")
    for r in results:
        print(f"  {r.title} -> {r.href}")
except NoResultsException as e:
    print(f"'python site:github.com': NoResults - {e}")

# Test 3: Query builder
try:
    q = Query("python").site("github.com")
    results = g.search(str(q), max_results=5)
    print(f"Query builder: got {len(results)} results")
except NoResultsException as e:
    print(f"Query builder: NoResults - {e}")
