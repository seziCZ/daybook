#!/usr/bin/env bash
# Monday morning. This week holds two ADR items of 2h, so that the user's
# "my ADR work" names exactly two items.
set -euo pipefail
bash "$(dirname "${BASH_SOURCE[0]}")/../fixtures/seed-home.sh"
cat > workspace-home/tasks.md <<'TASKS'
# Tasks

## Today

## This week
- [ ] Draft the ADR options and the decision drivers est:2h
- [ ] Write the ADR migration section est:2h
- [ ] Get the load test results from Petra est:15m waiting:Petra since:2026-10-22

## Backlog
- [ ] Prepare the team offsite agenda est:1h

## Done
- [x] Review Petra's pull request for the cache layer est:1h done:2026-10-30
- [x] Send the architecture summary to Jan est:30m done:2026-10-29
TASKS
sed -i 's/^last_evening: .*/last_evening: 2026-10-30/' workspace-home/state/routine.md
