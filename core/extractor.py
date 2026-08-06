import re


NUMBER_WORDS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10
}


def extract_number(text):

    m = re.search(r"\d+", text)

    if m:

        return int(m.group())

    for word, value in NUMBER_WORDS.items():

        if word in text.lower():

            return value

    return None


def extract_delay(text):

    m = re.search(
        r"after\s+(\d+)\s+seconds?",
        text.lower()
    )

    if m:

        return int(m.group(1))

    for word, value in NUMBER_WORDS.items():

        if f"after {word} second" in text.lower():

            return value

    return 0


def extract_theme(text):

    THEMES = (
        "matrix",
        "cyber",
        "minimal",
        "ubuntu",
        "ironman"
    )

    text = text.lower()

    for theme in THEMES:

        if theme in text:

            return theme

    return None


def extract_on_off(text):

    text = text.lower()

    if any(
        x in text
        for x in (
            "turn on",
            "switch on",
            "enable",
            "activate"
        )
    ):

        return "on"

    if any(
        x in text
        for x in (
            "turn off",
            "switch off",
            "disable",
            "deactivate"
        )
    ):

        return "off"

    return None

