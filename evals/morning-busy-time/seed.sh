#!/usr/bin/env bash
# Friday was closed by the evening routine: Today is empty and last_evening is 2026-10-30.
set -euo pipefail
bash "$(dirname "${BASH_SOURCE[0]}")/../fixtures/seed-home.sh"
cat > workspace-home/tasks.md <<'EOF'
# Tasks

## Today

## This week
- [ ] Draft the Q3 budget estimate for Maria est:2h due:2026-11-04
- [ ] Write the ADR for the event schema est:larger
  - [ ] Draft the options and the decision drivers est:2h
- [ ] Get the load test results from Petra est:15m waiting:Petra since:2026-10-22

## Backlog
- [ ] look into the flaky CI job
- [ ] Prepare the team offsite agenda est:1h

## Done
- [x] Review Petra's pull request for the cache layer est:1h done:2026-10-30
- [x] Send the architecture summary to Jan est:30m done:2026-10-29
EOF
sed -i 's/^last_evening: .*/last_evening: 2026-10-30/' workspace-home/state/routine.md
