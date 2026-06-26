#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Inject _tools/search-widget.html into index.html just before </body></html>.
Idempotent: replaces an existing block between the SEARCH-WIDGET markers.
Run after every rebuild of index.html (or wire the snippet into build_wiki_html.py)."""
import os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
WIKI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
idx = os.path.join(WIKI, "index.html")
snippet = open(os.path.join(WIKI, "_tools", "search-widget.html"), encoding="utf-8").read().strip()

html = open(idx, encoding="utf-8").read()
pat = re.compile(r"<!-- SEARCH-WIDGET START.*?SEARCH-WIDGET END -->", re.S)
if pat.search(html):
    html = pat.sub(snippet, html, count=1)
    action = "replaced"
else:
    assert "</body></html>" in html, "no </body></html> anchor in index.html"
    html = html.replace("</body></html>", "\n" + snippet + "\n</body></html>", 1)
    action = "inserted"
open(idx, "w", encoding="utf-8").write(html)
print(f"search widget {action} in index.html")
