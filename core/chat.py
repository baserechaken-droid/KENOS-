from datetime import datetime


def greeting():

    hour = datetime.now().hour

    if hour < 12:
        return "☀ Good morning, Ken."

    if hour < 18:
        return "🌤 Good afternoon, Ken."

    return "🌙 Good evening, Ken."


RESPONSES = {

    "hello":
        lambda: greeting(),

    "hi":
        lambda: greeting(),

    "hey":
        lambda: greeting(),

    "good morning":
        lambda: "☀ Good morning, Ken.",

    "good afternoon":
        lambda: "🌤 Good afternoon, Ken.",

    "good evening":
        lambda: "🌙 Good evening, Ken.",

    "how are you":
        lambda: "I'm operating normally and ready to help.",

    "who are you":
        lambda: "I am Jarvis, your KenOS assistant.",

    "thank you":
        lambda: "You're welcome, Ken.",

    "thanks":
        lambda: "You're welcome, Ken.",

    "good job":
        lambda: "Thank you, Ken.",

    "bye":
        lambda: "Goodbye, Ken.",

    "goodbye":
        lambda: "Goodbye, Ken."

}


def reply(text):

    text = text.lower().strip()

    func = RESPONSES.get(text)

    if func:

        return func()

    return None

