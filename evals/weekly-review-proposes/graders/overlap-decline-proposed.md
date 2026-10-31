---
type: llm
focus: last_message
---

Today is Friday 2026-11-06. The user asked for the weekly review, and the assistant may show several review steps in one message. Next week has: "Vendor intro" Wed 10:00 to 10:30, unanswered, organized by sales@vendor.example, an unknown contact; "Roadmap sync" Mon 14:00 to 15:00, unanswered, organized by Jan Novotny, overlapping the accepted "Customer workshop" 14:00 to 15:30; the weekly "Architecture guild" series that the user declined on 2026-10-29 and 2026-11-05; Tuesday fully booked by "Platform training" 09:00 to 17:00. Done this week: the API design doc review, the Q3 budget estimate, the customer demo slides. Waiting since 2026-10-22: load test results from Petra, older than the 7 day Nudge after.

PASS if, for "Roadmap sync", the message proposes to decline because it overlaps "Customer workshop", asks about it separately from the other invitation, and makes clear that Jan, the organizer, gets the answer. FAIL otherwise.
