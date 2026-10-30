#!/usr/bin/env bash
# Shared by every case: copies the fictional home folder into the run's workspace.
set -euo pipefail
cp -r "$(dirname "${BASH_SOURCE[0]}")/home" ./workspace-home
