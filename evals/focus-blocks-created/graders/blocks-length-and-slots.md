---
type: llm
focus: trace
---

Today is Monday 2026-11-02, 08:45, Europe/Prague. The profile sets working time 09:00 to 17:00 and `Focus block: 90m`. This week's calendar has these busy times:
- every day: Standup 09:00 to 09:15;
- Monday 2026-11-02: 1-on-1 Maria 13:00 to 13:30, Team sync 14:00 to 16:00;
- Tuesday 2026-11-03: Customer workshop 10:00 to 16:00;
- Wednesday 2026-11-04: Hiring interviews 09:30 to 12:00;
- Thursday 2026-11-05: Sprint review 11:00 to 12:30;
- Friday 2026-11-06: Sprint retro 10:00 to 11:00.

The user asked for focus time for two ADR items of 2h each. The assistant proposed two blocks: "Draft the ADR options and the decision drivers" on Monday 2026-11-02 10:00 to 11:30, and "Write the ADR migration section" on Wednesday 2026-11-04 13:00 to 14:30. The user approved both. Judge only the `create_event` calls in the trace. The mock calendar does not return created events in later lists, so ignore what the assistant says about checking them afterwards.

PASS if all of these hold:
- There are exactly two `create_event` calls, one for each ADR item.
- Each event lasts 90 minutes, the Focus block of the profile.
- Each event starts and ends between 09:00 and 17:00 Europe/Prague, from Monday 2026-11-02 to Friday 2026-11-06, and overlaps none of the busy times above.
- Each event has the day and the start time of the proposed block for its item. A time without a UTC offset is Europe/Prague time.

FAIL if any of these is false.
