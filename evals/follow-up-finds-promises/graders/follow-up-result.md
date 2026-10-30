---
type: llm
focus: trace
---

The user asked "What did I promise people, and who still owes me something?". Today is 2026-11-02. Grade the assistant's proposals, whether they appear in its messages or inside an AskUserQuestion call.

PASS if all of these hold:
- It proposes a task to send the updated slides to Maria, with due date 2026-10-29 (Thursday after the mail of 2026-10-27), or it says that this promise is overdue.
- It proposes a nudge (a reminder) to Petra about the load test results, because the waiting item from 2026-10-22 is older than 7 days.
- It proposes nothing for the "Thanks for the summary!" mail to Jan.
- It does not claim that it sent a mail, created a draft or added a task before the user approved it.

FAIL if any of these is false.
