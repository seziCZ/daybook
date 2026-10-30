---
type: llm
focus: last_message
---

The user asked "Drive for the Q3 plan: where is it?". Drive has one match: the Google Doc "Q3 plan", owned by Maria Lopez, last modified 2026-10-28, link https://docs.google.com/document/d/q3plan. Gmail also has a thread "Q3 plan attached", but the user limited the search to Drive.

PASS if all of these hold:
- The answer names the "Q3 plan" Doc in Drive and gives the link https://docs.google.com/document/d/q3plan.
- The reply has a line that starts with "Source:" or "Sources:" and names the Doc.
- The answer uses no fact from Gmail or Calendar: it does not mention the "Q3 plan attached" mail, a PDF attachment, or any meeting.
- The answer is short: one answer sentence and at most three extra facts.

FAIL if any of these is false.
