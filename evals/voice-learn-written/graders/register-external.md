---
type: regex
target:
  source: file
  path: workspace-home/voice.md
pattern: '## [^\n]*(External|[Pp]artner|[Cc]lient)[^\n]*\n[\s\S]*?Greeting:[^\n]*Dear (Mr |Ms )?<name>,[\s\S]*?Sign-off:[^\n]*Kind regards,[^\n]*Alex Novak[\s\S]*?Samples:'
weight: 2
---
