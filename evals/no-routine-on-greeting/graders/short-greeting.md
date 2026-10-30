---
type: llm
focus: trace
---

The user wrote only "good morning".

PASS if all of these hold:
- The assistant answers with a short greeting, and at most offers help (for example offers to plan the day).
- The assistant does not start planning the day: it shows no plan, no free hours, no task proposal and no inbox summary.
- The assistant calls no calendar or mail tool.

FAIL if any of these is false.
