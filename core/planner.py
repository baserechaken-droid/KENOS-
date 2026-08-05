import re


def split_tasks(text):

    text = text.lower().strip()

    tasks = []


    #
    # Torch sequence handling
    #

    if "flashlight" in text or "torch" in text:

        if "turn on" in text:

            tasks.append(
                {
                    "plugin": "torch",
                    "args": ["on"],
                    "delay": 0
                }
            )


        off_delay = 0


        match = re.search(
            r"after\s+(\d+)\s*seconds?",
            text
        )


        if match:

            off_delay = int(
                match.group(1)
            )


        if "turn it off" in text or "turn off" in text:

            tasks.append(
                {
                    "plugin": "torch",
                    "args": ["off"],
                    "delay": off_delay
                }
            )


        return tasks



    #
    # General command splitting
    #

    parts = re.split(
        r"\s+then\s+",
        text
    )


    for part in parts:

        part = part.strip()


        tasks.append(
            {
                "text": part,
                "delay": 0
            }
        )


    return tasks
