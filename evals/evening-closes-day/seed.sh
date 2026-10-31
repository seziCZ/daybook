#!/usr/bin/env bash
# Monday afternoon. Today holds Monday's plan: one item checked, one done but not checked, one open next step of a larger item.
set -euo pipefail
bash "$(dirname "${BASH_SOURCE[0]}")/../fixtures/seed-home.sh"
cat > workspace-home/tasks.md <<'TASKS'
# Tasks

## Today
Plan 2026-11-02: end 16:30, free 09:15 to 13:00, 13:30 to 17:00.
- [x] 09:15 Draft the Q3 budget estimate for Maria est:2h due:2026-11-04
- [ ] 13:30 Prepare the team offsite agenda est:1h
- [ ] 14:30 Draft the options and the decision drivers est:2h (step of: Write the ADR for the event schema)

## This week
- [ ] Write the ADR for the event schema est:larger
- [ ] Get the load test results from Petra est:15m waiting:Petra since:2026-10-22

## Backlog
- [ ] look into the flaky CI job

## Done
- [x] Review Petra's pull request for the cache layer est:1h done:2026-10-30
- [x] Send the architecture summary to Jan est:30m done:2026-10-29
TASKS
sed -i -e 's/^last_morning: .*/last_morning: 2026-11-02/' -e 's/^last_evening: .*/last_evening: 2026-10-30/' workspace-home/state/routine.md
