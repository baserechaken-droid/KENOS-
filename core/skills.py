import json
import os


SKILL_FILE = os.path.join(
    os.path.dirname(__file__),
    "skills.json"
)


def load_skills():

    try:

        with open(SKILL_FILE, "r") as f:

            return json.load(f)

    except Exception:

        return {}



def detect_intent(text):

    text = text.lower()

    skills = load_skills()


    for intent, words in skills.items():

        for word in words:

            if word in text:

                return intent


    return None
