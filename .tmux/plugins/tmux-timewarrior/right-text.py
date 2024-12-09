#!/usr/bin/env python3

import subprocess
from datetime import datetime
from tasklib import TaskWarrior

text = "no active task"
old_status_bg = subprocess.run(["tmux", "show-option", "-gqv", "status-bg"],
                               text=True, capture_output=True,
                               check=True).stdout.strip()
new_status_bg = "red"

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
    text = "active task is not assigned to any project"
    taskid = task["id"]
    if task["project"] is not None:
        project = task["project"]
        desc = task["description"]
        text = f"{project} ({taskid}): {desc} {
            hours:02}:{minutes:02}:{seconds:02}"
        new_status_bg = "green"
elif len(tasks) > 1:
    text = "more than one task active"

if old_status_bg != new_status_bg:
    subprocess.run(["tmux", "set", "-g", "status-bg", new_status_bg])

print(text)
