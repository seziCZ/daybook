#!/usr/bin/env bash
# Default home. The replay also gets the note that the recorded first turn wrote,
# so that the second turn sees the same files. The recording itself starts without it.
set -euo pipefail
here="$(dirname "${BASH_SOURCE[0]}")"
bash "$here/../fixtures/seed-home.sh"
if [ -f "$here/history.jsonl" ]; then
  cp "$here/note/2026-11-02 Q3 budget review (Maria).md" ./workspace-home/notes/meetings/
fi
