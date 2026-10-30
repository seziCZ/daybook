---
type: llm
focus: trace
---

The task list has the item "Get the load test results from Petra" with `waiting:Petra since:2026-10-22`. Today is 2026-11-02 and the profile sets `Nudge after: 7d`, so the item is 11 days old and overdue for a reminder. The user approved the groom proposal with "apply".

PASS if the assistant's messages in this session name the waiting item on Petra as old or overdue (for example "waiting 11 days"), or offer a reminder to Petra.

Showing a reminder draft to the user for review is fine, when the approved proposal included a reminder.

FAIL if the waiting item on Petra is not mentioned at all, or if the assistant says that it sent a mail or saved a draft to Gmail without the user approving that draft.
