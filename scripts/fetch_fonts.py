#!/usr/bin/env python3
"""Fetch the exact WOFF2 files Google serves for the site's font stack,
keep only latin + latin-ext subsets, and emit a self-hosted @font-face
stylesheet with local URLs."""
import os, re, time, urllib.request

CSS_URL = ("https://fonts.googleapis.com/css2?"
           "family=Inter:wght@400;500;600;700&"
           "family=Merriweather:ital,wght@0,400;0,700;1,400&"
           "family=Fira+Code:wght@400;500&display=swap")

# Chrome UA -> Google returns woff2 (oldest UA would get ttf/eot).
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

ROOT = "/home/dino/AgenticEngineering/ponor/ponor_website"
FONT_DIR = os.path.join(ROOT, "assets/fonts")
CSS_OUT = os.path.join(ROOT, "assets/css/fonts.css")
KEEP = {"latin", "latin-ext"}

os.makedirs(FONT_DIR, exist_ok=True)

def get(url, binary=False):
    # Network here is intermittent; retry with backoff on any transient error.
    last = None
    for attempt in range(8):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read() if binary else r.read().decode("utf-8")
        except Exception as e:
            last = e
            time.sleep(2 * (attempt + 1))
    raise last

css = get(CSS_URL)

# Google emits: /* subset */\n@font-face { ... }
blocks = re.findall(r"/\*\s*([\w-]+)\s*\*/\s*(@font-face\s*\{.*?\})", css, re.S)
out, saved = [], []
for subset, block in blocks:
    if subset not in KEEP:
        continue
    fam = re.search(r"font-family:\s*'([^']+)'", block).group(1)
    weight = re.search(r"font-weight:\s*(\d+)", block).group(1)
    style = re.search(r"font-style:\s*(\w+)", block).group(1)
    url = re.search(r"url\((https://[^)]+\.woff2)\)", block).group(1)
    slug = fam.lower().replace(" ", "-")
    name = f"{slug}-{weight}{'-italic' if style=='italic' else ''}-{subset}.woff2"
    dest = os.path.join(FONT_DIR, name)
    if not (os.path.exists(dest) and os.path.getsize(dest) > 0):
        open(dest, "wb").write(get(url, binary=True))
    block = re.sub(r"url\(https://[^)]+\.woff2\)",
                   f"url('/assets/fonts/{name}')", block)
    out.append(f"/* {fam} {weight}{' italic' if style=='italic' else ''} — {subset} */\n{block}")
    saved.append(name)

header = ("/* Self-hosted fonts (Inter, Merriweather, Fira Code).\n"
          "   Regenerated via scripts/fetch_fonts.py — do not hand-edit.\n"
          "   Only latin + latin-ext subsets are shipped (Bosnian needs\n"
          "   latin-ext for č/ć/ž/š/đ). */\n\n")
open(CSS_OUT, "w").write(header + "\n\n".join(out) + "\n")
print(f"Wrote {CSS_OUT}")
print(f"Downloaded {len(saved)} woff2 files to assets/fonts/:")
for n in saved:
    print("  ", n)
