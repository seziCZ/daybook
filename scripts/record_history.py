"""Records the first turn of an approval case as its history file.

Usage: python -I -B scripts/record_history.py <case-name> [<case-name> ...]

An approval case has two turns. `first-turn.md` holds the request, the skill
proposes a change and asks, and `prompt.md` holds the user's answer, such as
"apply". This script runs the first turn once with `claude plugin eval`, takes
the recorded session from the kept run folder, removes personal data with
`sanitize_history.py`, and writes `evals/<case>/history.jsonl`.

Re-record a case whenever a skill that it uses changes, because the history
contains the text of the skills at the time of recording.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EVALS = ROOT / "evals"


def record(name):
    case = EVALS / name
    first_turn = case / "first-turn.md"
    if not first_turn.exists():
        sys.exit(f"{name}: no first-turn.md")

    # A sibling case without the history: same files, the first turn as the prompt.
    probe = EVALS / f"zz-record-{name}"
    if probe.exists():
        shutil.rmtree(probe)
    shutil.copytree(case, probe, ignore=shutil.ignore_patterns("history.jsonl", "graders", "prompt.md"))
    yaml = (probe / "case.yaml").read_text(encoding="utf-8")
    yaml = re.sub(r"^  history_file: .*\n", "", yaml, flags=re.M)
    yaml = re.sub(r"^name: .*$", f"name: zz-record-{name}", yaml, flags=re.M)
    (probe / "case.yaml").write_text(yaml, encoding="utf-8", newline="\n")
    shutil.copy(first_turn, probe / "prompt.md")
    (probe / "graders").mkdir()
    (probe / "graders" / "ran.md").write_text("---\ntype: tool_used\ntool: Read\n---\n", encoding="utf-8", newline="\n")

    out = Path(tempfile.mkdtemp()) / "record.json"
    run_dir = None
    try:
        subprocess.run(
            ["claude", "plugin", "eval", ".", "--case", probe.name, "--runs", "1", "--ablation", "none",
             "--model", "sonnet", "--scaffold", "--allow-tools", "Write", "Edit", "--trust-plugin",
             "--no-publish", "--keep-temp", "--json", str(out)],
            cwd=ROOT, check=False, shell=sys.platform == "win32")
        run = json.loads(out.read_text(encoding="utf-8"))["cases"][0]["arms"]["with"][0]
        if run.get("tracePath"):
            run_dir = Path(run["tracePath"]).parent.parent
        if run.get("error"):
            sys.exit(f"{name}: the first turn failed: {run['error']}")
        sessions = list((run_dir / "config" / "projects").glob("*/*.jsonl"))
        if len(sessions) != 1:
            sys.exit(f"{name}: expected one recorded session in {run_dir}, found {len(sessions)}")
        subprocess.run(
            [sys.executable, "-I", "-B", str(ROOT / "scripts" / "sanitize_history.py"),
             str(sessions[0]), str(run_dir), str(case / "history.jsonl")], check=True)
    finally:
        # The run folder holds the raw session with account data, so it never stays.
        if run_dir:
            shutil.rmtree(run_dir, ignore_errors=True)
        shutil.rmtree(probe, ignore_errors=True)
        shutil.rmtree(out.parent, ignore_errors=True)


failed = []
for case_name in sys.argv[1:] or sys.exit(__doc__):
    try:
        record(case_name)
    except (SystemExit, subprocess.CalledProcessError) as e:
        print(f"{case_name}: not recorded: {e}", file=sys.stderr)
        failed.append(case_name)
if failed:
    sys.exit(f"not recorded: {', '.join(failed)}")
