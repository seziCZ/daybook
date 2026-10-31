#!/usr/bin/env bash
set -euo pipefail
case_dir="$(dirname "${BASH_SOURCE[0]}")"
bash "$case_dir/../fixtures/seed-home.sh"
# The last scan was a week ago. The first turn moves last_scan to today
# without asking, because the skill writes its own state line.
last_scan=2026-10-26
# The replay starts from the files that the recorded first turn left behind.
if [ -f "$case_dir/history.jsonl" ]; then last_scan=2026-11-02; fi
printf '# Mail follow-up state\n\nWritten by: mail-follow-up (last_scan).\n\nlast_scan: %s\n' "$last_scan" > ./workspace-home/state/mail-follow-up.md
