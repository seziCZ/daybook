#!/usr/bin/env bash
# Default home, but Friday is closed and no task covers Maria's estimate yet,
# so that triage proposes it as a new task instead of "no action".
set -euo pipefail
bash "$(dirname "${BASH_SOURCE[0]}")/../fixtures/seed-home.sh"
cat > workspace-home/tasks.md <<'TASKS'
# Tasks

## Today

## This week
- [ ] Write the ADR for the event schema est:larger
  - [ ] Draft the options and the decision drivers est:2h
- [ ] Get the load test results from Petra est:15m waiting:Petra since:2026-10-22

## Backlog
- [ ] Prepare the team offsite agenda est:1h

## Done
- [x] Review Petra's pull request for the cache layer est:1h done:2026-10-30
- [x] Send the architecture summary to Jan est:30m done:2026-10-29
TASKS
sed -i 's/^last_evening: .*/last_evening: 2026-10-30/' workspace-home/state/routine.md
