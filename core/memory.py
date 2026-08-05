import json
import os

FILE = "data/memory.json"


class Memory:

    def __init__(self):

        self.data = self.load()


    def load(self):

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(FILE):

            return {}

        try:

            with open(FILE) as f:

                return json.load(f)

        except:

            return {}


    def save(self):

        with open(FILE, "w") as f:

            json.dump(
                self.data,
                f,
                indent=4
            )


    def remember(self, key, value):

        self.data[key.lower()] = value

        self.save()


    def recall(self, key):

        return self.data.get(key.lower())


    def forget(self, key):

        if key.lower() in self.data:

            del self.data[key.lower()]

            self.save()


    def all(self):

        return dict(self.data)


memory = Memory()

