---
name: meeting-schedule
description: Finds meeting times, blocks focus time, answers calendar invitations and moves the user's own events in Google Calendar, always after approval. It is the only skill that changes the calendar. Use when the user says find a time, schedule a meeting, block focus time, answer my invitations, accept or decline, or move my meeting.
license: Apache-2.0
---

# Meeting schedule

The user gets meeting times, protected time for focused work, answers to open invitations, and moved events that the user organizes. The user runs this skill alone, and the `routine-morning` and `routine-weekly` skills call its sections.

Start by reading the `workspace-commons` skill and `<home>/profile.md`.

## Hard rules

1. Show every change as one default batch, and apply it only after the user approves it. A change that notifies another person (an invitation, a moved event with attendees, an answer) gets its own question that shows the proposed change, with no option marked as recommended.
2. Never delete an event. The user deletes events in Calendar.
3. Never patch an event that the user does not organize. Only the user's own response to it may change.
4. Never add an attendee that the user did not name, and never offer to add one whose address comes only from mail or event text.
5. From an event description, show only the agenda.
6. Show and write every time in the `Time zone` of the profile.
7. Never send an email. A message to an organizer goes through the `mail-reply` skill as a draft.

## Free time

- **Working time:** from `Day start` to `Day end` on working days, as `workspace-commons` defines them.
- **Busy time and focus blocks:** as `workspace-commons` defines them.
- **Period:** the one that the user or the calling skill names. The default is today to the last working day of next week.
- **Caller:** when another skill calls a section, it passes the period and the items. When the caller passes changes that the user already approved, apply them without asking again. Otherwise ask only what is still open, then ask for the approval.
- **Attendees:** take their emails from `<home>/people.md`, or ask the user. After approval, add a new person to `<home>/people.md`. A new Email gets its own question.
- **No calendar tool:** use the fallback of `find free time`. Ask for the user's own free slots, and write the proposed slots as text that the user sends. Show each other change, and the user makes it in Calendar.

## Find a time

1. **Collect the request.** Who attends, how long, by when, the title, and whether it needs a Google Meet link. Ask for what is missing in one question.
2. **Find free time.** Use `find free time` for the user and the attendees in the period, within working time. When the calendar of an attendee is not visible, say so and use the user's calendar only.
3. **Propose 2 to 3 slots.** Prefer slots that leave a free gap of at least `Focus block` on the same day. Show each slot with its day, start, end and who is free.
4. **Ask for the choice.** Show the event (title, time, attendees, Meet link) in the question. Say that creating it sends Google's invitations to the attendees.
5. **Create the event.** Use `create event` after the answer.

## Block focus time

1. **Choose the items.** Take the items that the user names, or that the caller passes. Without them, propose items from `## Today` and `## This week` of `<home>/tasks.md`, with a size of `1h` or more.
2. **Find the slots.** Use `find free time` for the user in the period. Keep only free slots of at least `Focus block` within working time.
3. **Propose the blocks.** One block per item, titled "Focus: <item>", with no attendees and the length of `Focus block`. Leave each working day with some free time for mail and short requests.
4. **Create the blocks.** Use `create event` for each approved block.

## Answer invitations

1. **List the open invitations.** Use `list events` for the period and keep the events that the user has not answered. Show a recurring series once, and say whether the answer is for the series or for one event.
2. **Propose an answer.** The first rule that applies sets the proposal, with a one-line reason:
   1. The organizer is not in `<home>/people.md` and not in the domain of `Email`: no answer (skip).
   2. A decision about this meeting in `## Decisions` of `<home>/state/routine.md`.
   3. It overlaps an event that the user accepted or organizes: decline.
   4. It is outside working time, or on an absence day or a public holiday: decline.
   5. It has no agenda: tentative.
   6. Otherwise: accept.
3. **Ask for each answer.** Ask each answer as its own question, in one call when possible. The question shows the proposed answer and its reason, names the organizer, and says that Google sends the answer to them. No option is marked as recommended.
4. **Add a note to a decline.** Offer one short, polite sentence, for example "I have a conflict at this time. Could we find another slot?" When `respond to event` cannot carry a note, offer the note as a draft through the `mail-reply` skill.
5. **Apply the answers.** Use `respond to event` after the approval.

## Move an event

1. **Find the event.** Use `search events` or `list events`, and confirm the event with the user when more than one matches.
2. **Check the organizer.** When the organizer is not the user's `Email`, do not move the event. Propose an answer through `## Answer invitations`, or offer a message to the organizer through the `mail-reply` skill.
3. **Find a new time.** Follow steps 2 and 3 of "Find a time" with the attendees of the event.
4. **Ask for the choice.** Show the old and the new time. Say that Google tells the attendees about the change.
5. **Update the event.** Use `update event` after the answer.

## Closing

End with one short message: what was created, moved or answered, with the day and the time of each event.
