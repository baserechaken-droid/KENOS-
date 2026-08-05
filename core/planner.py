import re

from core.actions import extract_delay


def split_tasks(text):

    text = text.strip()

    parts = re.split(
        r"\b(?:and|then|after that|afterwards|next)\b",
        text,
        flags=re.I
    )

    tasks = []

    for part in parts:

        part = part.strip()

        if not part:
            continue

        command, delay = extract_delay(part)

        tasks.append({

            "text": command,

            "delay": delay

        })

    return tasks
