import re


DELAY_PATTERN = re.compile(
    r"\bafter\s+(\d+)\s+(seconds?|minutes?)\b",
    re.IGNORECASE
)


def extract_delay(text):

    if not isinstance(text, str):

        return "", 0

    text = text.strip()

    delay = 0

    match = DELAY_PATTERN.search(text)

    if match:

        value = int(match.group(1))

        unit = match.group(2).lower()

        if unit.startswith("minute"):

            delay = value * 60

        else:

            delay = value

        text = DELAY_PATTERN.sub("", text)

    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    return text, delay
