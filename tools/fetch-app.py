#!/usr/bin/env python3
"""Pull max reviews (newest first) + listing for App Store apps.

usage: fetch-app.py [--extra] name=appid [name=appid ...]
  --extra  also pull gb/ca/au reviews (tagged by country) for more volume
Output:  research-data/<name>/{reviews.json,negatives.md,listing.json}
Reruns merge into reviews.json, so history keeps growing past the RSS window.
"""
import json, os, sys, time, urllib.request

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "research-data")
SORTS = ["mostrecent", "mosthelpful"]  # ponytail: RSS caps 10 pages x 50 per sort; union ~1000/app/country


def get(url):
    for i in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30) as r:
                return r.read()
        except Exception as e:
            err = e
            time.sleep(1 + i)
    raise err


def reviews(app_id, country):
    out = {}
    for sort in SORTS:
        for page in range(1, 11):
            try:
                d = json.loads(get(f"https://itunes.apple.com/{country}/rss/customerreviews/page={page}/id={app_id}/sortby={sort}/json"))
            except Exception as e:
                print(f"  {country} {sort} p{page}: {e}"); break
            es = d.get("feed", {}).get("entry", [])
            es = [es] if isinstance(es, dict) else es
            es = [e for e in es if "im:rating" in e]
            if not es:
                break
            for e in es:
                rid = e["id"]["label"]
                out[rid] = {"id": rid, "country": country, "rating": int(e["im:rating"]["label"]),
                            "title": e["title"]["label"], "text": e["content"]["label"],
                            "author": e["author"]["name"]["label"], "version": e.get("im:version", {}).get("label"),
                            "updated": e["updated"]["label"]}
            time.sleep(0.4)
    return out


def main():
    args = sys.argv[1:]
    countries = ["us"] + (["gb", "ca", "au"] if "--extra" in args else [])
    for a in [x for x in args if "=" in x]:
        name, app_id = a.split("=", 1)
        d = os.path.join(ROOT, name); os.makedirs(d, exist_ok=True)

        # listing metadata (iTunes lookup)
        info = json.loads(get(f"https://itunes.apple.com/lookup?id={app_id}&country=us"))["results"][0]
        json.dump(info, open(os.path.join(d, "listing.json"), "w"), indent=2)

        # reviews: merge with previous runs, newest first
        path = os.path.join(d, "reviews.json")
        merged = {r["id"]: r for r in json.load(open(path))} if os.path.exists(path) else {}
        before = len(merged)
        for c in countries:
            merged.update(reviews(app_id, c))
        rows = sorted(merged.values(), key=lambda r: r["updated"], reverse=True)
        json.dump(rows, open(path, "w"), ensure_ascii=False, indent=1)
        neg_rows = [r for r in rows if r["rating"] <= 2]
        neg = len(neg_rows)
        # compact file for pasting into a chat: ~65 tokens/review, fits a context window
        with open(os.path.join(d, "negatives.md"), "w", encoding="utf-8") as f:
            f.write(f"# {name} 1-2 star reviews, newest first ({neg})\n# stars|date|version|country|title: text\n")
            for r in neg_rows:
                t = " ".join(r["text"].split())
                f.write(f"{r['rating']}|{r['updated'][:10]}|{r['version']}|{r['country']}|{r['title']}: {t}\n")
        print(f"{name}: {len(rows)} reviews (+{len(rows)-before} new), {neg} are 1-2 star, "
              f"{rows[-1]['updated'][:10]}..{rows[0]['updated'][:10]}")


main()
