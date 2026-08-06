import re


def parse(plugin, text):

    text = text.lower().strip()

    #
    # Torch
    #

    if plugin == "torch":

        if any(
            x in text for x in (
                "on",
                "enable",
                "activate"
            )
        ):
            return ["on"]

        if any(
            x in text for x in (
                "off",
                "disable",
                "deactivate"
            )
        ):
            return ["off"]

    #
    # Theme
    #

    if plugin == "theme":

        for theme in (
            "matrix",
            "cyber",
            "ubuntu",
            "minimal",
            "ironman"
        ):

            if theme in text:

                return [theme]

    #
    # Volume
    #

    if plugin == "volume":

        m = re.search(r"(\d+)", text)

        if m:

            return [m.group(1)]

        if "up" in text or "increase" in text:

            return ["up"]

        if "down" in text or "decrease" in text:

            return ["down"]

    #
    # Remember
    #

    if plugin == "remember":

        m = re.search(
            r"remember(?: that)? my (.+?) is (.+)",
            text
        )

        if m:

            return [
                m.group(1).strip(),
                m.group(2).strip()
            ]

    #
    # Recall
    #

    if plugin == "recall":

        m = re.search(
            r"(?:what is|what's|whats) my (.+)",
            text
        )

        if m:

            return [
                m.group(1).strip()
            ]

    return []

