"""Turns a recorded Claude Code session into an eval history file.

Usage: python -I -B scripts/sanitize_history.py <session.jsonl> <run-temp-dir> <out.jsonl>

A recorded session holds more than the conversation: the system prompt, the
account's email and organization, and the local paths of the run. This script
keeps only the user and assistant messages, replaces the run directory with a
neutral path, and refuses to write the file when personal data is left.

Set EVAL_FORBIDDEN to a regex of your own words (for example your name) to
check for them too.
"""
import json
import os
import re
import sys

KEEP = {"user", "assistant"}
NEUTRAL = "C:\\eval\\run"


def leaks(text):
    """Personal data that must never be in a history file."""
    found = set()
    for email in re.findall(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", text):
        domain = email.split("@", 1)[1].lower()
        if not (domain.endswith(".example") or domain == "example.com" or domain.endswith(".example.com")):
            found.add(email)
    found.update(re.findall(r"[A-Za-z]:\\\\Users\\\\[^\\\"]+|/(?:Users|home)/[^/\"]+", text))
    if '"session_context"' in text or '"userEmail"' in text:
        found.add("session context")
    extra = os.environ.get("EVAL_FORBIDDEN")
    if extra:
        found.update(m.group(0) for m in re.finditer(extra, text, re.I))
    return found


def main():
    src, run_dir, out = sys.argv[1], sys.argv[2].rstrip("\\/"), sys.argv[3]
    replacements = [
        (json.dumps(run_dir)[1:-1], json.dumps(NEUTRAL)[1:-1]),
        (json.dumps(run_dir.replace("\\", "/"))[1:-1], "C:/eval/run"),
    ]
    lines = []
    for raw in open(src, encoding="utf-8"):
        entry = json.loads(raw)
        if entry.get("type") not in KEEP:
            continue
        text = json.dumps(entry, ensure_ascii=False)
        for old, new in replacements:
            text = text.replace(old, new)
        lines.append(text)
    found = sorted(set().union(*(leaks(line) for line in lines)) if lines else set())
    if found:
        sys.exit(f"refusing to write {out}: personal data left: {found}")
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print(f"wrote {out}: {len(lines)} entries")


if __name__ == "__main__":
    main()
