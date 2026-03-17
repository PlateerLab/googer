from googer import Googer

with Googer() as g:
    results = g.search("2025한국시리즈 우승팀")
    for r in results:
        print(r.title)
