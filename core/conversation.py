from collections import deque
from datetime import datetime


class Conversation:

    def __init__(self):

        self.history = deque(maxlen=20)

        self.topic = None


    def add(self, speaker, text):

        self.history.append(
            {
                "speaker": speaker,
                "text": text,
                "time": datetime.now().strftime("%H:%M:%S")
            }
        )


    def set_topic(self, topic):

        self.topic = topic


    def get_topic(self):

        return self.topic


    def last(self, count=5):

        return list(self.history)[-count:]


    def clear(self):

        self.history.clear()

        self.topic = None


conversation = Conversation()

