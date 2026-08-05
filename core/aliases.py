ALIASES = {

    #
    # Time
    #

    "time": "time",
    "clock": "time",
    "current time": "time",

    #
    # Date
    #

    "date": "date",
    "today": "date",
    "calendar": "date",

    #
    # Battery
    #

    "battery": "battery",
    "charge": "battery",
    "power": "battery",

    #
    # Dashboard
    #

    "dashboard": "dashboard",
    "overview": "dashboard",
    "system dashboard": "dashboard",

    #
    # Notes
    #

    "note": "notes",
    "notes": "notes",
    "memo": "notes",

    #
    # Camera
    #

    "camera": "photo",
    "photo": "photo",
    "picture": "photo",

    #
    # Music
    #

    "music": "music",
    "song": "music",
    "audio": "music",

    #
    # WiFi
    #

    "wifi": "wifi",
    "wireless": "wifi",
    "internet": "wifi",

    #
    # Volume
    #

    "volume": "volume",
    "sound": "volume",
    "speaker": "volume",

    #
    # Flashlight
    #

    "flashlight": "torch",
    "flash light": "torch",
    "torch": "torch",
    "lamp": "torch",

    #
    # Settings
    #

    "settings": "settings",
    "preferences": "settings",
    "config": "settings"

}


def find_alias(text):

    text = text.lower()

    for alias, plugin in ALIASES.items():

        if alias in text:

            return plugin

    return None

