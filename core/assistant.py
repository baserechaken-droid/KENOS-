from services.voice.engine import voice


class Assistant:

    def __init__(self):

        self.name = "Jarvis"
        self.owner = "Ken"
        self.awake = True

    def greet(self):

        message = (
            "Welcome back Ken. "
            "KenOS is online and ready."
        )

        print(f"🤖 {self.name}: {message}")

        try:
            voice.speak(message)
        except:
            pass

    def acknowledge(self):

        message = "Yes Ken?"

        print(f"🤖 {self.name}: {message}")

        try:
            voice.speak(message)
        except:
            pass

    def confirm(self, text):

        print(f"🤖 {self.name}: {text}")

        try:
            voice.speak(text)
        except:
            pass


assistant = Assistant()
