import random


class Personality:

    def __init__(self):

        self.name = "Jarvis"

        self.confirmations = [
            "Done.",
            "Completed.",
            "Finished.",
            "Task completed.",
            "Consider it done."
        ]

        self.listening = [
            "Yes Ken?",
            "Listening.",
            "How may I help?",
            "Ready.",
            "Awaiting your command."
        ]

        self.errors = [
            "I couldn't complete that.",
            "That command isn't available.",
            "Please try again.",
            "I don't recognize that command."
        ]

    def confirmation(self):
        return random.choice(self.confirmations)

    def listening_reply(self):
        return random.choice(self.listening)

    def error(self):
        return random.choice(self.errors)


personality = Personality()
