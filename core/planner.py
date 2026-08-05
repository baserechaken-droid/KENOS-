import re


CONNECTORS = r"\s+(?:then|and then|after that|next|finally)\s+"

TORCH_WORDS = (
    "torch",
    "flashlight",
    "flash light",
    "lamp",
    "light",
)

ON_WORDS = (
    "turn on",
    "switch on",
    "enable",
    "activate",
    "start",
)

OFF_WORDS = (
    "turn off",
    "switch off",
    "disable",
    "deactivate",
    "stop",
)

LAST_DEVICE = None


def parse_delay(text):

    m = re.search(
        r"after\s+(\d+)\s*(second|seconds|sec|secs)",
        text
    )

    if m:
        return int(m.group(1))

    m = re.search(
        r"after\s+(\d+)\s*(minute|minutes|min|mins)",
        text
    )

    if m:
        return int(m.group(1)) * 60

    return 0


def detect_device(text):

    global LAST_DEVICE

    for word in TORCH_WORDS:

        if word in text:

            LAST_DEVICE = "torch"

            return "torch"

    if (
        LAST_DEVICE == "torch"
        and (
            " it " in f" {text} "
            or text.startswith("it ")
            or " it" in text
        )
    ):
        return "torch"

    return None


def detect_action(text):

    for w in ON_WORDS:

        if w in text:
            return "on"

    for w in OFF_WORDS:

        if w in text:
            return "off"

    return None


def split_tasks(text):

    global LAST_DEVICE

    text = text.lower().strip()

    LAST_DEVICE = None

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

        device = detect_device(part)

        action = detect_action(part)

        if device == "torch" and action:

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
