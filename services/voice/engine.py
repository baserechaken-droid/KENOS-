import json
import subprocess
import os


CONFIG = "data/voice.json"


class VoiceEngine:


    def __init__(self):

        self.settings = self.load()



    def load(self):

        try:

            with open(CONFIG) as f:
                return json.load(f)

        except:

            return {
                "enabled": False
            }



    def speak(self, text):

        if not self.settings.get("enabled"):
            return


        message = str(text)


        try:

            subprocess.run(
                [
                    "termux-tts-speak",
                    "-r",
                    str(self.settings.get("speed",1.0)),
                    message
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

        except:

            pass



    def status(self):

        return self.settings



voice = VoiceEngine()
