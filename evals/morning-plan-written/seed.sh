#!/usr/bin/env bash
# Friday was closed by the evening routine: Today is empty and last_evening is 2026-10-30.
# No raw capture in the Backlog, so that the inbox step has nothing to propose and the first proposal is the plan.
# The first turn (in history.jsonl) already wrote last_morning: 2026-11-02 in step 1, so the seed starts from that state.
set -euo pipefail
bash "$(dirname "${BASH_SOURCE[0]}")/../fixtures/seed-home.sh"
cat > workspace-home/tasks.md <<'TASKS'
# Tasks

## Today

## This week
- [ ] Draft the Q3 budget estimate for Maria est:2h due:2026-11-04
- [ ] Write the ADR for the event schema est:larger
  - [ ] Draft the options and the decision drivers est:2h
- [ ] Get the load test results from Petra est:15m waiting:Petra since:2026-10-22

## Backlog
- [ ] Prepare the team offsite agenda est:1h

## Done
- [x] Review Petra's pull request for the cache layer est:1h done:2026-10-30
- [x] Send the architecture summary to Jan est:30m done:2026-10-29
TASKS
sed -i -e 's/^last_morning: .*/last_morning: 2026-11-02/' -e 's/^last_evening: .*/last_evening: 2026-10-30/' workspace-home/state/routine.md
