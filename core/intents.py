import re


def detect(text):

    text = text.lower().strip()

    #
    # Remember
    #

    m = re.match(
        r"remember (?:that )?my (.+?) is (.+)",
        text
    )

    if m:

        return (
            "remember",
            [
                m.group(1).strip(),
                m.group(2).strip()
            ]
        )

    #
    # Recall
    #

    m = re.match(
        r"(?:what is|what's|whats) my (.+)",
        text
    )

    if m:

        return (
            "recall",
            [
                m.group(1).strip()
            ]
        )

    #
    # Forget
    #

    m = re.match(
        r"forget (?:my )?(.+)",
        text
    )

    if m:

        return (
            "forget",
            [
                m.group(1).strip()
            ]
        )

    #
    # Time
    #

    if re.search(
        r"(what('?s| is)? the time|time now|current time)",
        text
    ):

        return ("time", [])

    #
    # Date
    #

    if re.search(
        r"(today('?s)? date|current date|what('?s| is)? the date)",
        text
    ):

        return ("date", [])

    #
    # Battery
    #

    if "battery" in text:

        return ("battery", [])

    #
    # Dashboard
    #

    if "dashboard" in text:

        return ("dashboard", [])

    #
    # Torch ON
    #

    if (
        ("flash" in text or "torch" in text)
        and any(
            w in text for w in (
                "turn on",
                "switch on",
                "enable",
                "activate"
            )
        )
    ):

        return (
            "torch",
            ["on"]
        )

    #
    # Torch OFF
    #

    if (
        ("flash" in text or "torch" in text)
        and any(
            w in text for w in (
                "turn off",
                "switch off",
                "disable",
                "deactivate"
            )
        )
    ):

        return (
            "torch",
            ["off"]
        )

    return None

