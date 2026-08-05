import json
import subprocess
import threading
import queue
import os

CONFIG = "data/voice.json"


class VoiceEngine:

    def __init__(self):

        self.settings = self.load()

        self.queue = queue.Queue()

        self.worker = threading.Thread(
            target=self._worker,
            daemon=True
        )

        self.worker.start()


    def load(self):

        try:

            with open(CONFIG) as f:

                return json.load(f)

        except:

            return {
                "enabled": True,
                "speed": 1.15,
                "pitch": 0.90,
                "voice": "jarvis"
            }


    def save(self):

        os.makedirs("data", exist_ok=True)

        with open(CONFIG, "w") as f:

            json.dump(
                self.settings,
                f,
                indent=4
            )


    def _worker(self):

        while True:

            text = self.queue.get()

            if text is None:

                break

            try:

                subprocess.run(
                    [
                        "termux-tts-speak",
                        "-r",
                        str(self.settings.get("speed", 1.15)),
                        "-p",
                        str(self.settings.get("pitch", 0.90)),
                        str(text)
                    ],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )

            except:

                pass

            self.queue.task_done()


    def speak(self, text):

        if not self.settings.get("enabled", True):

            return

        while not self.queue.empty():

            try:

                self.queue.get_nowait()

                self.queue.task_done()

            except:

                break

        self.queue.put(str(text))


    def wait(self):

        self.queue.join()


    def stop(self):

        self.queue.put(None)


    def status(self):

        return self.settings


voice = VoiceEngine()

