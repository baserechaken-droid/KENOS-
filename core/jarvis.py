from core.nlp import parse
from core.memory import remember as save_memory
from core.memory import recall as load_memory


class Jarvis:

    def __init__(self):

        self.history = []

    def reply(self, text):

        text = text.strip()

        if not text:
            return None, None

        self.history.append(text)

        intent = parse(text)

        if intent.command:
            return intent.command, intent.args

        return None, None

    def remember(self, key, value):

        save_memory(key, value)

    def recall(self, key):

        return load_memory(key)

    def last(self):

        if not self.history:
            return None

        return self.history[-1]

    def clear(self):

        self.history.clear()


jarvis = Jarvis()
