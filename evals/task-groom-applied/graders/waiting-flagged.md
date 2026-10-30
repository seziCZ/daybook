---
type: llm
focus: trace
---

The task list has the item "Get the load test results from Petra" with `waiting:Petra since:2026-10-22`. Today is 2026-11-02 and the profile sets `Nudge after: 7d`, so the item is 11 days old and overdue for a reminder. The user approved the groom proposal with "apply".

PASS if the assistant's messages in this session name the waiting item on Petra as old or overdue (for example "waiting 11 days"), or offer a reminder to Petra.

FAIL if the waiting item on Petra is not mentioned at all, or if the assistant sent or drafted a mail to Petra without the user asking for it.
