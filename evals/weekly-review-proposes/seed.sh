#!/usr/bin/env bash
# Friday 2026-11-06 afternoon. Default home, with three items done this week,
# an empty Today (no plan left open) and the last weekly review one week ago.
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
- [ ] look into the flaky CI job
- [ ] Prepare the team offsite agenda est:1h

## Done
- [x] Review Jan's API design doc est:1h done:2026-11-05
- [x] Draft the Q3 budget estimate for Maria est:2h due:2026-11-04 done:2026-11-04
- [x] Prepare the customer demo slides est:1h done:2026-11-03
- [x] Review Petra's pull request for the cache layer est:1h done:2026-10-30
- [x] Send the architecture summary to Jan est:30m done:2026-10-29
TASKS
sed -i -e 's/^last_morning: .*/last_morning: 2026-11-06/' -e 's/^last_evening: .*/last_evening: 2026-11-05/' -e 's/^last_weekly: .*/last_weekly: 2026-10-30/' workspace-home/state/routine.md
