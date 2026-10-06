#!/usr/bin/env python3
"""Build the research site from the first 12 research category folders.

Reads Harshil's product-strategy.md for each category when available and writes
site/index.html from tools/research-site.html. Run from anywhere:
    python3 tools/build-research-site.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "tools" / "research-site.html"
OUT = ROOT / "site" / "index.html"
CATEGORIES = ROOT / "vault" / "research" / "categories"
STRATEGIES = ROOT / "vault" / "members" / "harshil" / "drafts"

NAMES = {"tv": "TV"}


def title(slug):
    return " ".join(NAMES.get(w, w.capitalize()) for w in slug.split("-"))


def parse(path):
    text = path.read_text(encoding="utf-8")
    meta, body = {}, text
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if m:
        body = text[m.end():]
        for line in m.group(1).splitlines():
            k, sep, v = line.partition(":")
            if sep:
                meta[k.strip()] = v.strip()
    # Wikilinks point at notes the site doesn't carry; keep the label as text.
    body = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", body)
    body = re.sub(r"\[\[([^\]]+)\]\]", lambda m: m.group(1).rsplit("/", 1)[-1], body)
    return meta, body


def main():
    cats = []
    for category_dir in sorted(p for p in CATEGORIES.iterdir() if p.is_dir())[:12]:
        slug = category_dir.name
        path = STRATEGIES / slug / "product-strategy.md"
        meta, body = parse(path) if path.is_file() else ({}, "")
        cats.append({
            "slug": slug,
            "name": title(slug),
            "member": meta.get("member", ""),
            "updated": meta.get("updated", ""),
            "status": meta.get("status", "") if body else "coming soon",
            "md": body,
        })
    data = json.dumps(cats, ensure_ascii=False).replace("</", "<\\/")
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(TEMPLATE.read_text(encoding="utf-8").replace("__DATA__", data), encoding="utf-8")
    assert len(cats) == 12 and "__DATA__" not in OUT.read_text(encoding="utf-8")
    print(f"{len(cats)} categories, {sum(bool(c['md']) for c in cats)} strategies -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
