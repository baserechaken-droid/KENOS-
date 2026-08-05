import re


CONNECTORS = (
    r"\s+(?:then|and then|after that|next|finally)\s+"
)


TORCH_ON = (
    "turn on",
    "switch on",
    "enable",
    "start",
    "activate",
)


TORCH_OFF = (
    "turn off",
    "switch off",
    "disable",
    "stop",
    "deactivate",
)


TORCH_WORDS = (
    "torch",
    "flashlight",
    "flash light",
    "light",
    "lamp",
)


def parse_delay(text):

    delay = 0

    match = re.search(
        r"after\s+(\d+)\s*(second|seconds|sec|secs)",
        text
    )

    if match:
        delay = int(match.group(1))

    match = re.search(
        r"after\s+(\d+)\s*(minute|minutes|min|mins)",
        text
    )

    if match:
        delay = int(match.group(1)) * 60

    return delay


def is_torch(text):

    text = text.lower()

    return any(
        word in text
        for word in TORCH_WORDS
    )


def torch_action(text):

    text = text.lower()

    for word in TORCH_ON:

        if word in text:
            return "on"

    for word in TORCH_OFF:

        if word in text:
            return "off"

    return None


def split_tasks(text):

    text = text.lower().strip()

    tasks = []

    parts = re.split(
        CONNECTORS,
        text
    )

    for part in parts:

        part = part.strip()

        if not part:
            continue

        delay = parse_delay(part)

        if is_torch(part):

            action = torch_action(part)

            if action:

                tasks.append(
                    {
                        "plugin": "torch",
                        "args": [action],
                        "delay": delay
                    }
                )

                continue

        tasks.append(
            {
                "text": part,
                "delay": delay
            }
        )

    return tasks
