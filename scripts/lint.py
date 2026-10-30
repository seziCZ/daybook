"""Checks the coherence of the skill-garden repository.

Run from the repository root: python -I -B scripts/lint.py
Exits 1 when it finds a problem. Uses only the Python standard library.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import sanitize_history  # noqa: E402
SKILLS = ROOT / "skills"
COMMONS_REF = SKILLS / "workspace-commons" / "references"
problems = []


def problem(path, msg):
    problems.append(f"{path.relative_to(ROOT).as_posix()}: {msg}")


def read(path):
    return path.read_text(encoding="utf-8")


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        if re.match(r"^[a-z-]+:", line):
            key, _, value = line.partition(":")
            fields[key] = value.strip()
    return fields


skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
skill_names = {p.name for p in skill_dirs}
skill_text = {p.name: read(p / "SKILL.md") for p in skill_dirs if (p / "SKILL.md").exists()}

# Contract: capabilities, profile keys and home files.
cap_text = read(COMMONS_REF / "capabilities.md")
capabilities = set(re.findall(r"^\| `([a-z]+(?: [a-z]+)+)` \|", cap_text, re.M))
home_text = read(COMMONS_REF / "home.md")
profile_keys = set(re.findall(r"^\| [A-Z][a-z]+(?: [a-z]+)* \| `([^`]+)` \|", home_text, re.M))
profile_keys.add("Public holidays")
home_files = {"profile.md", "tasks.md", "people.md", "voice.md", "notes", "state/routine.md",
              "state/meeting-assist.md", "state/mail-follow-up.md", "state/<file>.md"}
cap_verbs = ("search", "read", "list", "create", "update", "find", "respond", "recent")

for name, text in skill_text.items():
    path = SKILLS / name / "SKILL.md"
    fm = frontmatter(text)
    if fm is None:
        problem(path, "missing frontmatter")
        continue
    if set(fm) != {"name", "description", "license"}:
        problem(path, f"frontmatter must have exactly name, description, license (has {sorted(fm)})")
    if fm.get("name") != name:
        problem(path, f"name '{fm.get('name')}' does not match the folder")
    desc = fm.get("description", "")
    if len(desc) > 400:
        problem(path, f"description has {len(desc)} characters (max 400)")
    if "<" in desc or ">" in desc:
        problem(path, "description contains an angle bracket")
    if not re.search(r"\bUse (when|for|only)\b", desc):
        problem(path, "description has no 'Use when', 'Use for' or 'Use only' trigger")
    if fm.get("license") != "Apache-2.0":
        problem(path, "license must be Apache-2.0")
    lines = text.count("\n") + 1
    if lines > 120:
        problem(path, f"{lines} lines (max 120)")

    for ref in re.findall(r"`([a-z]+-[a-z-]+)` skill", text):
        if ref not in skill_names:
            problem(path, f"names unknown skill `{ref}`")
    for section, ref in re.findall(r"`## ([^`]+)` of the `([a-z-]+)` skill", text):
        if ref in skill_text and not re.search(rf"^## {re.escape(section)}$", skill_text[ref], re.M):
            problem(path, f"section '## {section}' not found in `{ref}`")
    for cap in re.findall(r"`([a-z]+ [a-z]+(?: [a-z]+)?)`", text):
        if cap.split()[0] in cap_verbs and cap not in capabilities:
            problem(path, f"unknown capability `{cap}`")
    for key in re.findall(r"`([A-Z][A-Za-z ]+)` (?:of|in) the profile", text):
        if key not in profile_keys:
            problem(path, f"unknown profile key `{key}`")
    for ref in re.findall(r"<home>/([\w./<>-]+)", text):
        ref = ref.rstrip(".,;:)")
        if ref.endswith("/"):
            ref = ref[:-1]
        if ref not in home_files and not ref.startswith(("notes", "<Meeting")):
            problem(path, f"unknown home file <home>/{ref}")

# Plain text: no em dash or en dash in prose.
prose = [ROOT / "README.md", *ROOT.joinpath("docs").glob("*.md"), ROOT / "evals" / "README.md",
         *SKILLS.rglob("*.md")]
for path in prose:
    for i, line in enumerate(read(path).splitlines(), 1):
        if "–" in line or "—" in line:
            problem(path, f"line {i} has an em dash or en dash")

# Manifests.
for name in ("plugin.json", "marketplace.json"):
    path = ROOT / ".claude-plugin" / name
    try:
        json.loads(read(path))
    except (OSError, ValueError) as e:
        problem(path, f"invalid JSON: {e}")

# Eval cases: harness copy, plugin entries and graders.
evals = ROOT / "evals"
harness = evals / "fixtures" / "harness"
for case in sorted(p for p in evals.iterdir() if (p / "case.yaml").exists()):
    yaml = read(case / "case.yaml")
    if 'plugins: ["../..", "harness"]' not in yaml:
        problem(case / "case.yaml", 'plugins must be ["../..", "harness"]')
    for f in harness.rglob("*"):
        if f.is_file():
            copy = case / "harness" / f.relative_to(harness)
            if not copy.exists() or read(copy) != read(f):
                problem(case, f"harness/{f.relative_to(harness).as_posix()} differs from fixtures/harness")
    graders = list((case / "graders").glob("*.md"))
    if not graders:
        problem(case, "has no graders")
    negative_only = "trigger" in re.search(r"^tags: \[(.*)\]", yaml, re.M).group(1)
    if not negative_only and not any("type: tool_used" in read(g) and not re.search(r"^min: 0", read(g), re.M) for g in graders):
        problem(case, "has no control grader (tool_used that must be called)")
    for g in graders:
        if "target: mock_calls" in read(g):
            problem(g, "uses target: mock_calls, which is not reliable")
    for skill in re.findall(r"\(\?:\[\\w-\]\+:\)\?([a-z-]+)", "".join(read(g) for g in graders)):
        if skill not in skill_names:
            problem(case, f"grader names unknown skill {skill}")
    for stray in case.rglob("*.jsonl"):
        if stray.name != "history.jsonl":
            problem(stray, "only history.jsonl may be committed; the runner writes raw sessions with account data here")
        found = sanitize_history.leaks(read(stray))
        if found:
            problem(stray, f"personal data: {sorted(found)}")
    history = case / "history.jsonl"
    if "history_file:" in yaml:
        if not history.exists() or not (case / "first-turn.md").exists():
            problem(case, "an approval case needs history.jsonl and first-turn.md")

for p in problems:
    print(p)
print(f"{len(skill_text)} skills checked, {len(problems)} problems")
sys.exit(1 if problems else 0)
