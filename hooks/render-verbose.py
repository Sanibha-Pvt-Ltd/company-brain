#!/usr/bin/env python3
"""Render a write-only verbose .jsonl into a readable activity mirror.

The mirror exists so that humans and later sessions have something to read that is not
the raw log — re-reading the .jsonl mid-session is what the write-only rule forbids.
"""
import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

MAX_ROWS = 400  # ponytail: a 2000-call session renders its last 400; raise if it bites


def parse(path):
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if line:
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def local(ts):
    try:
        return (
            datetime.fromisoformat(ts.replace("Z", "+00:00"))
            .astimezone()
        )
    except ValueError:
        return None


def summarize(rec):
    """One line describing the call, from whatever the tool put in its input."""
    try:
        inp = json.loads(rec.get("input") or "{}")
    except json.JSONDecodeError:
        inp = {}
    if not isinstance(inp, dict):
        inp = {}
    for key in ("command", "file_path", "pattern", "path", "url", "query", "prompt"):
        val = inp.get(key)
        if isinstance(val, str) and val.strip():
            one = " ".join(val.split())
            return one[:110] + ("…" if len(one) > 110 else "")
    return ""


def projects_touched(records, dst):
    """`[[projects/<slug>]]` for every cwd in the log that has a project note.

    The cwd is already in every record; the slug is the directory basename lowercased,
    which is exactly what bin/seed-projects.sh names the note. Without this an activity
    mirror links nothing and sits in the graph as an orphan dot.
    """
    vault = dst.parent.parent.parent  # vault/logs/activity/x.md -> vault/
    slugs = []
    home = Path(os.environ.get("SANIBHA_HOME", Path.home() / "Sanibha"))
    for cwd in dict.fromkeys(r.get("cwd") or "" for r in records):
        p = Path(cwd)
        # inside ~/Sanibha the project is the first directory under it; elsewhere the basename
        slug = (p.relative_to(home).parts[0] if home in p.parents else p.name).lower().replace(" ", "-")
        if slug and (vault / "projects" / f"{slug}.md").exists() and slug not in slugs:
            slugs.append(slug)
    return slugs


def render(src, dst):
    records = list(parse(src))
    if not records:
        return

    stem = src.stem
    date = stem.split("_")[0]
    key = stem.split("_")[-1]
    tools = Counter(r.get("tool", "?") for r in records)
    stamps = [t for t in (local(r.get("ts", "")) for r in records) if t]
    span = ""
    if len(stamps) >= 2:
        mins = int((stamps[-1] - stamps[0]).total_seconds() // 60)
        if mins:
            span = f"{mins // 60}h {mins % 60}m"

    out = [
        "---",
        "type: activity",
        f"date: {date}",
        f"calls: {len(records)}",
        f"session_key: {key}",
        f"member: {os.environ.get('BRAIN_NAME', 'unknown')}",
        f'verbose: "[[logs/verbose/{stem}]]"',
        f"updated: {datetime.now(timezone.utc).astimezone():%Y-%m-%d}",
        "---",
        "",
        f"# Activity — {date}",
        "",
        f"{len(records)} tool calls" + (f" over {span}" if span else "") + ".",
        "",
    ]
    touched = projects_touched(records, dst)
    if touched:
        out += ["Projects: " + ", ".join(f"[[projects/{s}]]" for s in touched), ""]
    out += [
        "| Tool | Calls |",
        "| --- | ---: |",
    ]
    out += [f"| {t} | {n} |" for t, n in tools.most_common()]
    out += ["", "## Calls", "", "| Time | Tool | What |", "| --- | --- | --- |"]

    shown = records[-MAX_ROWS:]
    if len(shown) < len(records):
        out.insert(-2, f"_Showing the last {MAX_ROWS} of {len(records)} calls._\n")
    for r in shown:
        t = local(r.get("ts", ""))
        what = summarize(r).replace("|", "\\|")
        flag = "" if r.get("ok", True) else " ⚠"
        out.append(f"| {t:%H:%M:%S} | {r.get('tool', '?')}{flag} | {what} |" if t
                   else f"| — | {r.get('tool', '?')}{flag} | {what} |")

    dst.write_text("\n".join(out) + "\n", encoding="utf-8")


def demo():
    """Self-check: assert-based, no framework."""
    import tempfile

    with tempfile.TemporaryDirectory() as d:
        vault = Path(d) / "vault"
        (vault / "projects").mkdir(parents=True)
        (vault / "projects" / "hermes.md").write_text("---\ntype: project\n---\n")
        (vault / "logs" / "activity").mkdir(parents=True)
        src = Path(d) / "2026-08-13_014302_abcd1234.jsonl"
        dst = vault / "logs" / "activity" / "mirror.md"
        src.write_text(
            '{"ts":"2026-08-13T01:43:02Z","tool":"Bash","input":"{\\"command\\":\\"ls -la\\"}",'
            '"cwd":"/Users/x/dev/Hermes","ok":true}\n'
            '{"ts":"2026-08-13T02:13:02Z","tool":"Edit","input":"{\\"file_path\\":\\"/a/b.py\\"}",'
            '"cwd":"/Users/x/dev/no-such-project","ok":false}\n'
            "not json\n"
        )
        render(src, dst)
        text = dst.read_text()
        assert "type: activity" in text
        assert "session_key: abcd1234" in text
        assert "calls: 2" in text, text
        assert "| Bash | 1 |" in text
        assert "ls -la" in text
        assert "⚠" in text, "failed calls must be flagged"
        assert "0h 30m" in text, "span must be computed"
        assert "[[projects/hermes]]" in text, "cwd with a project note must be linked"
        assert "no-such-project" not in text, "a cwd with no note must not become a link"

        empty = Path(d) / "empty.jsonl"
        empty.write_text("")
        missing = Path(d) / "none.md"
        render(empty, missing)
        assert not missing.exists(), "an empty log must not produce a mirror"
    print("ok")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "--demo":
        demo()
    elif len(sys.argv) == 3:
        render(Path(sys.argv[1]), Path(sys.argv[2]))
    else:
        sys.exit("usage: render-verbose.py <verbose.jsonl> <mirror.md> | --demo")
