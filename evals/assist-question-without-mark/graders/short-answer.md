---
type: llm
focus: last_message
---

The user is in a meeting and typed "what did Maria say about the budget deadline" without a question mark. Maria wrote on 2026-10-31 that she needs the platform cost estimate by Wednesday (4 November 2026).

PASS if all of these hold:
- The message answers the question: Maria needs the cost estimate by Wednesday (4 November). Mentioning that the earlier note had her confirmation of the deadline still open is fine.
- The message names a source, such as Gmail with the subject or the date.
- The answer is at most four lines of plain sentences, without a table, headers or bullets.
- The message does not treat the text as a remark: it does not say "Noted" or that it stored the text.

FAIL if any of these is false.
