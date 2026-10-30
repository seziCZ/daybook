---
type: llm
focus: last_message
---

The user asked "When did Maria last write to me about the Q3 plan?".

PASS if all of these hold:
- The answer says that Maria last wrote about the Q3 plan on 28 October 2026 (any date format), not on 15 October.
- The reply has one line that starts with "Source:" or "Sources:" and names the subject "Re: Q3 plan", the date 2026-10-28 and the link https://mail.google.com/mail/u/0/#all/thr-502.
- The answer is short: one answer sentence and at most three extra facts, with no list of every match.

FAIL if any of these is false.
