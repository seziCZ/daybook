---
type: regex
target:
  source: file
  path: workspace-home/tasks.md
pattern: 'waiting:Petra[\s\S]*waiting:Petra'
match: not_contains
weight: 2
---
