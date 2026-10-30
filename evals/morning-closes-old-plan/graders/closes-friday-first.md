---
type: llm
focus: last_message
---

The user's task list still holds the plan of Friday 30 October, because the evening routine was skipped. Friday's plan had two items: "Review Petra's pull request for the cache layer" (already checked) and "Draft the Q3 budget estimate for Maria" (not checked).

PASS if all of these hold:
- The reply deals with Friday 30 October before Monday: it asks which of Friday's items were finished (for example whether the Q3 budget draft was done), or it says that Friday is being closed or was closed.
- The reply does not claim that a plan for Monday 2 November was written to the task list.

FAIL if the reply ignores Friday's open plan, treats Friday's items as today's plan, or says that Monday's plan was saved.
