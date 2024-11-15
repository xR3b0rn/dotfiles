#!/usr/bin/env python3

from datetime import datetime
from tasklib import TaskWarrior

text = "#[bg=red]no active task"

tw = TaskWarrior("~/.task")

tasks = tw.tasks.pending().filter("+ACTIVE")
if len(tasks) == 1:
    task = tasks[0]
    start = task["start"]
    start = start.replace(tzinfo=None)
    now = datetime.now()
    now = now.replace(tzinfo=None)
    delta = now - start
    total_seconds = int(delta.total_seconds())
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    text = "#[bg=red]active task is not assigned to any project"
    if task["project"] is not None:
        project = task["project"]
        desc = task["description"]
        text = f"#[bg=green]{project}: {desc} {
            hours:02}:{minutes:02}:{seconds:02}"
elif len(tasks) > 1:
    text = "#[bg=red]more than one task active"

print(text)
