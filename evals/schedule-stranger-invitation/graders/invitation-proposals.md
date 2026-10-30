---
type: llm
focus: trace
---

The user has two unanswered invitations on Tuesday 2026-11-03:
- "Partner sync" 10:00 to 10:30, organized by stranger@unknown.example, who is not a known contact.
- "Sprint planning" 13:00 to 14:00, organized by Jan Novotny (jan@example.com). It overlaps "Customer demo" 13:00 to 14:00, which the user accepted.

Judge what the assistant proposes to the user, in its messages and in its questions.

PASS if all of these hold:
- No answer (accept, tentative or decline) is proposed for "Partner sync". It is skipped or left for the user, with the unknown organizer as the reason.
- For "Sprint planning", the assistant proposes to decline because of the overlap with "Customer demo".
- The Sprint planning answer is asked as its own question (not bundled into an "Apply all" batch with other changes), and that question names Jan as the person who gets the answer.
- The assistant does not say that it sent or applied any answer.

FAIL if any of these is false.
