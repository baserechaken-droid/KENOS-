ALIASES = {
    "turn on flashlight": ("torch", ["on"]),
    "turn off flashlight": ("torch", ["off"]),
    "turn on torch": ("torch", ["on"]),
    "turn off torch": ("torch", ["off"]),
    "flashlight on": ("torch", ["on"]),
    "flashlight off": ("torch", ["off"]),
    "battery level": ("battery", []),
    "battery status": ("battery", []),
    "how much battery do i have": ("battery", []),
    "wifi status": ("wifi", []),
    "check wifi": ("wifi", []),
    "open youtube": ("open", ["youtube"]),
    "open google": ("open", ["google"]),
}


def parse(text):

    text = text.lower().strip()

    if text in ALIASES:
        return ALIASES[text]

    words = text.split()

    if not words:
        return None

    return words[0], words[1:]
