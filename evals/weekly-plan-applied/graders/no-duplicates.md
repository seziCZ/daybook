---
type: regex
target:
  source: file
  path: workspace-home/tasks.md
pattern: 'Write the ADR for the event schema[\s\S]*Write the ADR for the event schema|Draft the options and the decision drivers[\s\S]*Draft the options and the decision drivers|offsite agenda[\s\S]*offsite agenda|flaky CI[\s\S]*flaky CI|load test results[\s\S]*load test results'
match: not_contains
weight: 2
---
