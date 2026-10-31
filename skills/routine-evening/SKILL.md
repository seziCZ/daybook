---
name: routine-evening
description: Ends the working day in a few minutes. Ticks what was done, writes down open thoughts, and closes the day. Plans nothing and starts nothing. Use when the user says "done for the day", "close the day", "end my day", or runs /routine-evening.
license: Apache-2.0
---

# Evening routine

The evening routine ends the working day in at most `Evening routine` minutes of the profile. The user stops work after it. It records the day and lets the user write down what is still on their mind. It plans nothing and starts nothing. The inbox, the calendar and the plan for tomorrow belong to the `routine-morning` skill.

Start by reading the `workspace-commons` skill and `<home>/profile.md`. Then read `<home>/tasks.md` and `<home>/state/routine.md`.

## Hard rules

1. The session is the three steps below, in this order, and nothing else. When the user says "stop", go to step 3.
2. Show no hours, counts or metrics in any message.
3. Never send an email or a chat message.
4. Change `<home>/tasks.md` only through the `task-list` skill.
5. When the user names work that they could do now (a reply, a fix, a decision), capture it in step 2. If they ask to do it now, answer: "It is captured for tomorrow. Do you still want to do it now?" If they say yes, show the closing message of step 3. End it with "The door is open again. Run the evening routine when you finish." Then do the work as a normal request.

## Steps

1. **Tick the day.** The day to close is the date on the `Plan` line of `## Today`, otherwise today. When the `routine-morning` skill runs this step, close the day that it passes. Then return to `routine-morning`, and do not end the morning session.
   - Read the events of the day with `list events`. Show them in one line, with the start time and the title only. For example: "Meetings: 09:30 Team standup, 14:00 Budget review with Maria." Without a calendar tool, leave the line out.
   - Show the items of the `## Today` section, numbered, without the `est:` and other fields. Checked items count as done.
   - Ask one checkbox question with the unchecked items: "Which of these did you finish?" The user can also name other work that they finished. When Today is empty, ask only "What did you finish today?" When the closed day is not today, ask "What did you finish on <day>?" instead.
   - Run `## End of day` of the `task-list` skill for the closed day, with the ticked items and the other finished work.
   - Write `last_evening: YYYY-MM-DD` (the closed day) in `<home>/state/routine.md`. Replace the old `last_evening:` line, or add it.

2. **Write down open thoughts.** Ask one plain question: "What is still on your mind about work? For the one that occupies you most, also name the next concrete step."
   - Each line of the answer becomes one raw capture at the top of the Backlog, through `## Capture` of the `task-list` skill. Keep the user's own words. Add no tag, size or order.
   - Skip a line that is already a raw capture in the Backlog.
   - When the user answers "nothing", end the step without a write.

3. **Close the door.** Show one closing message. It names in one line what the user finished today. For example: "Today you finished the budget reply to Maria and the onboarding checklist." It names no files and no numbers. It ends with "The door is closed. See you tomorrow."
   - When the next working day (see "Days, busy time and free hours" in `workspace-commons`) is not tomorrow, name that day and its date instead. For example: "See you on Monday, 2 November."
   - When the user finished nothing that they can name, write "Today is closed." in place of the line about the finished work.
   - The closing message needs no answer, and nothing follows it.

## Example

```
Meetings: 09:30 Team standup, 14:00 Budget review with Maria.
1. [x] Send the Q3 budget draft to Maria
2. [ ] Review the onboarding checklist for Alex
3. [ ] Book the venue for the team day
Which of these did you finish?
```

The user ticks 2. In step 2 they write "the venue is still open, next step: call two venues in the morning". The skill captures that line in the user's words. It closes with "Today you finished the budget draft and the onboarding checklist. The door is closed. See you on Monday, 2 November."
