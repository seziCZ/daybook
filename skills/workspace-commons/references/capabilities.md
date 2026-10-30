# Capability map

Each skill names its work as a capability. This map gives the tool for each backend. Connector tool names can carry a prefix (for example `mcp__gmail__search_threads`), so match the end of the name. When a tool is missing from the connector, use the next backend.

Run `gws` writes with `--dry-run` first, show the result, and then run them without it. Dates in `gws` are ISO 8601 with the time zone of the profile, for example `2026-11-02T09:00:00+01:00`.

## Mail

| Capability | Connector tool | `gws` command | Without a tool |
|---|---|---|---|
| `search mail` | `search_threads` with a Gmail query | `gws gmail users threads list --params '{"userId":"me","q":"<query>","maxResults":20}'` | Ask the user to name the mails that need action. |
| `read thread` | `get_thread` | `gws gmail users threads get --params '{"userId":"me","id":"<id>"}'` | Ask the user for the part that matters, in their own words. |
| `read message` | `get_message` | `gws gmail +read --id <id> --headers` | Ask the user for the part that matters, in their own words. |
| `list drafts` | `list_drafts` | `gws gmail users drafts list --params '{"userId":"me"}'` | Skip. |
| `create draft` | `create_draft` | `gws gmail users drafts create --params '{"userId":"me"}' --json '{"message":{"raw":"<base64url RFC 2822 message>","threadId":"<id>"}}'` | Show the text, and the user pastes it. |
| `update draft` | `update_draft` | `gws gmail users drafts update --params '{"userId":"me","id":"<draft id>"}' --json '{"message":{"raw":"<base64url RFC 2822 message>","threadId":"<id>"}}'` | Show the new text. |

A reply made with `gws` stays in its thread only when the raw message has the `In-Reply-To` and `References` headers of the last message and the same subject. Search results may not show who wrote the last message of a thread. Use `read thread` when that matters.

Useful Gmail queries: `in:inbox category:primary after:YYYY/MM/DD`, `from:<address>`, `in:sent after:YYYY/MM/DD`, `label:<name>`, `is:unread`.

## Calendar

| Capability | Connector tool | `gws` command | Without a tool |
|---|---|---|---|
| `list events` | `list_events` with a start and an end | Future: `gws calendar +agenda --today` (or `--tomorrow`, `--week`, `--days <n>`). Past: `gws calendar events list --params '{"calendarId":"primary","timeMin":"<ISO>","timeMax":"<ISO>","singleEvents":true,"orderBy":"startTime"}'` | Ask for the meetings and their times. |
| `read event` | `get_event` | `gws calendar events get --params '{"calendarId":"primary","eventId":"<id>"}'` | Ask for the details. |
| `search events` | `search_events` | `gws calendar events list --params '{"calendarId":"primary","q":"<text>","timeMin":"<ISO>","timeMax":"<ISO>","singleEvents":true}'` | Ask the user. |
| `find free time` | `suggest_time` | `gws calendar freebusy query --json '{"timeMin":"<ISO>","timeMax":"<ISO>","items":[{"id":"<email>"}]}'` | Ask for the user's own free slots, and write the proposed slots as text that the user sends. |
| `create event` | `create_event` | `gws calendar +insert --summary "<title>" --start <ISO> --end <ISO> [--attendee <email>] [--meet]` | Show the event, and the user creates it. |
| `update event` | `update_event` | `gws calendar events patch --params '{"calendarId":"primary","eventId":"<id>"}' --json '<changed fields>'` | Show the change, and the user makes it. |
| `respond to event` | `respond_to_event` | none | Tell the user which answer to give in Calendar. |

A response may not carry a note to the organizer. When a note matters, the `mail-reply` skill drafts it. Never patch an event that the user does not organize.

## Files

| Capability | Connector tool | `gws` command | Without a tool |
|---|---|---|---|
| `search files` | `search_files` | `gws drive files list --params "{\"q\":\"fullText contains '<text>' and trashed=false\",\"pageSize\":10}"` | Ask for a link. |
| `recent files` | `list_recent_files` | `gws drive files list --params '{"q":"trashed=false","orderBy":"modifiedTime desc","pageSize":10}'` | Skip. |
| `read file` | `read_file_content`, `read_doc` for a Doc, `read_presentation` for Slides | `gws drive files export --params '{"fileId":"<id>","mimeType":"text/plain"}'` | Ask the user for the part that matters, in their own words. |
| `read sheet` | `get_values` | `gws sheets +read --spreadsheet <id> --range "<range>"` | Ask for the values. |
| `create doc` | `create_file` with the Google Docs type | `gws docs documents create --json '{"title":"<title>"}'`, then `gws docs +write --document <id> --text "<text>"`, only with the id that `create` just returned | Write a Markdown file in the home instead. |

## Other sources

- **Home files:** read and write them directly with the agent's file tools. They need no capability.
- **Web:** use the agent's own web search, only when the user asks for it.

## Never use

These tools break the hard rules of the `workspace-commons` skill, even when they are available:

- Sending: `send_message`, `reply`, `forward`, `gws gmail +send`, `+reply`, `+reply-all`, `+forward`, `users drafts send`, `users messages send`.
- Removing or hiding: any `trash_`, `delete_`, `spam` or `label` tool, `gws gmail users messages trash`, `delete`, `modify`.
- Sharing: `share_file`, any change of permissions, `gws drive permissions`.
- Deleting events: `delete_event`, `gws calendar events delete`. The user deletes an event in Calendar.
- Editing existing files: `update_doc`, `update_file`, `copy_file`, `append_values`, `update_values`, `batch_clear_values`, `copy_sheet_to_another_spreadsheet`, `update_presentation`, `gws drive files update` or `copy`, and any `gws sheets`, `docs` or `slides` write to a file that this session did not create.
