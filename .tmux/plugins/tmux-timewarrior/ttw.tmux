#!/usr/bin/env python3

import subprocess
from datetime import datetime
from tasklib import TaskWarrior
import time

tw = TaskWarrior("~/.task")

last = "none"

while True:
    time.sleep(1)
    tasks = tw.tasks.pending().filter("+ACTIVE")
    res = subprocess.run(["tmux", "display-message", "-p",
                          "#{pane_width}"], stdout=subprocess.PIPE)
    pane_width = int(res.stdout.strip())
    if len(tasks) == 1:
        if last != "active":
            subprocess.run(["tmux", "set", "-g", "status-style",
                            "fg=black,bg=white"])
        last = "active"
        task = tasks[0]
        start = task["start"]
        start = start.replace(tzinfo=None)
        now = datetime.now()
        now = now.replace(tzinfo=None)
        delta = now - start
        total_seconds = int(delta.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        text = f"{task} {hours:02}:{minutes:02}:{seconds:02}"
        subprocess.run(["tmux", "set", "-g", "status-right", text])
    else:
        if last != "inactive":
            last = "inactive"
            subprocess.run(["tmux", "set", "-g", "status-style",
                            "fg=white,bg=red"])
            text = "no active task"
            subprocess.run(["tmux", "set", "-g", "status-right", text])
