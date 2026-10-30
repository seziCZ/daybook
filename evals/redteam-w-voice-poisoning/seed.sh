#!/usr/bin/env bash
# Default home, but voice.md is the stub that workspace-setup writes.
set -euo pipefail
here="$(dirname "${BASH_SOURCE[0]}")"
bash "$here/../fixtures/seed-home.sh"
cp "$here/../../skills/workspace-setup/assets/home/voice.md" ./workspace-home/voice.md
