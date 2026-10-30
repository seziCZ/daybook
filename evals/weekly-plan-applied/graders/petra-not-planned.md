---
type: regex
target:
  source: file
  path: workspace-home/tasks.md
pattern: '## This week(?:(?!## Backlog)[\s\S])*waiting:Petra'
match: not_contains
---
