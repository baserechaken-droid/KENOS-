from core.nlp import parse


class Jarvis:

    def __init__(self):

        self.history = []

    def reply(self, text):

        self.history.append(text)

        intent = parse(text)

        if intent.command:

            return intent.command, intent.args

        return None, None

    def remember(self, text):

        self.history.append(text)

    def last(self):

        if not self.history:

            return None

        return self.history[-1]

    def clear(self):

        self.history.clear()


jarvis = Jarvis()
