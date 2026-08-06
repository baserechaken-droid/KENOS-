from core.extractor import (
    extract_number,
    extract_delay,
    extract_theme,
    extract_on_off
)

import re


def parse(plugin, text):

    text = text.lower().strip()

    #
    # Torch
    #

    if plugin == "torch":

        args = []

        state = extract_on_off(text)

        if state:

            args.append(state)

        delay = extract_delay(text)

        if delay:

            args.append(str(delay))

        return args

    #
    # Theme
    #

    if plugin == "theme":

        theme = extract_theme(text)

        if theme:

            return [theme]

        return []

    #
    # Volume
    #

    if plugin == "volume":

        number = extract_number(text)

        if number is not None:

            return [str(number)]

        if "up" in text or "increase" in text:

            return ["up"]

        if "down" in text or "decrease" in text:

            return ["down"]

        return []

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

        return []

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

    #
    # Forget
    #

    if plugin == "forget":

        m = re.search(
            r"forget(?: my)? (.+)",
            text
        )

        if m:

            return [
                m.group(1).strip()
            ]

        return []

    return []

