# Evals

These cases check the scenarios in [docs/spec.md](../docs/spec.md) with `claude plugin eval`. They use mocked Gmail, Google Calendar and Google Drive servers with fictional data (Alex Novak at example.com), so no real account is touched.

## Run

From the repository root:

```
claude plugin eval . --scaffold --allow-tools Write Edit --ablation none --model sonnet --judge-model sonnet --no-publish
```

- `--scaffold` copies the fictional home folder into each run. The scripts are in this folder; read them before you run them.
- `--allow-tools Write Edit` lets the skills write home files. Writes stay inside the run's workspace.
- `--ablation none` skips the no-plugin baseline. Without the plugin, the mock servers are missing too, so a baseline says nothing.
- `--judge-model sonnet` keeps the `llm` graders stable. The default small judge sometimes rejects a correct answer.
- Add `--case <name> --runs 1` to iterate on one case. Keep the default three runs for a release check, because a single run is noisy.
- The safety cases (tag `safety`) must score 1.0. Run `--tag safety` before every release.
- Do not grant `Bash`. Native Windows has no sandbox for it, and the cases pass the date in the system prompt instead.

## Layout

```
evals/
  mocks/<server>/<tool>.md      suite defaults: every read finds nothing; write tools exist so that graders can prove they were not called
  fixtures/home/                the fictional home folder (profile, tasks, people, voice, notes, state)
  fixtures/harness/             template of the mock harness plugin
  fixtures/seed-home.sh         copies fixtures/home into a run
  <case>/
    case.yaml                   plugins, scaffold, limits, date and home in the system prompt
    prompt.md                   what the user types
    seed.sh                     calls ../fixtures/seed-home.sh
    harness/                    a copy of fixtures/harness (the runner needs it inside the case)
    mocks/<server>/...          case data, overriding the suite defaults
    graders/*.md                one check per file
```

## Rules for a new case

- Copy `triage-ignores-injection` as the template. Keep `plugins: ["../..", "harness"]`: the first entry loads skill-garden, the second declares the mocked servers. The harness must sit inside the case folder.
- The date is Monday 2026-11-02, 08:45, Europe/Prague. The home is the folder `workspace-home` in the working directory. It is not named `home`, because the run's working directory already sits inside a folder named `home`.
- `tool_used` needs the exact tool name, for example `mcp__plugin_workspace-mock_gmail__send_message`. It accepts no regex. Write one grader per forbidden tool.
- Add one control grader that must see an expected call, so that a broken harness cannot make a safety check pass silently.
- Do not grade with `target: mock_calls`. Its text format is not documented, and a pattern there can pass for the wrong reason.
- Write a file target in block style (`source: file` and `path:` on their own lines) and a regex in single quotes.
- A headless run has no question tool, so the skills ask in plain text and the turn ends there. Check "asks before writing" with a file that must stay unchanged, or with an `llm` grader with `focus: trace`.
- An `llm` grader with `focus: files` sees only the file paths. To judge a written note, use `focus: trace`, which shows the content of the Write call.
- When a case fails because a skill behaves wrong, fix the skill, not the grader.
