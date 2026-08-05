import re


def format_for_speech(text):

    if not text:
        return ""

    speech = text

    # Remove emojis
    speech = re.sub(
        r"[^\w\s.,:%/-]",
        "",
        speech
    )

    # Improve common phrases
    replacements = {

        "Battery:": "Your battery is",

        "Status:": "and the status is",

        "Flashlight ON": "I've turned on the flashlight.",

        "Flashlight OFF": "I've turned off the flashlight.",

        "Time:": "The current time is",

        "Date:": "Today's date is",

    }

    for old, new in replacements.items():

        speech = speech.replace(old, new)

    speech = " ".join(speech.split())

    return speech
