---
type: llm
focus: trace
---

The weekly review proposed a `## This week` for next week. The user answered: keep waiting on Petra, skip all calendar changes, no absences, and apply the This week plan as proposed.

The recorded proposal was, in this order:
1. Write the ADR for the event schema (est:larger), counting only its next step "Draft the options and the decision drivers" (2h).
2. Prepare the team offsite agenda (1h).
3. Look into the flaky CI job, with the proposed size 1h (it was a raw capture without a size).

Compare this proposal, and the proposal in the trace when the trace shows it, with the final content of `workspace-home/tasks.md` that the assistant wrote after the answer (the last Write or Edit of that file in the trace).

PASS if all of these hold:
- `## This week` holds exactly the proposed items, in the proposed order, and nothing else. A `larger` item may keep its sub-item.
- The waiting item "Get the load test results from Petra" is not in `## This week`. It is still an open item somewhere in the file (for example at the top of `## Backlog`), not deleted and not marked done.
- No item appears twice in the file, and no item was deleted.
- The items in `## Done` are unchanged.

FAIL if any of these is false, or if the trace shows no write of `workspace-home/tasks.md` after the answer.
