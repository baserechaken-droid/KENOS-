import subprocess
import json


class Device:

    @staticmethod
    def _run(command):

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True
            )

            return result.stdout.strip()

        except Exception:
            return None

    @staticmethod
    def battery():

        data = Device._run(["termux-battery-status"])

        if not data:
            return None

        return json.loads(data)

    @staticmethod
    def wifi():

        data = Device._run(["termux-wifi-connectioninfo"])

        if not data:
            return None

        return json.loads(data)

    @staticmethod
    def wifi_scan():

        data = Device._run(["termux-wifi-scaninfo"])

        if not data:
            return []

        return json.loads(data)

    @staticmethod
    def speak(text):

        subprocess.run(
            ["termux-tts-speak", text]
        )

    @staticmethod
    def torch(state):

        subprocess.run(
            [
                "termux-torch",
                "on" if state else "off"
            ]
        )

    @staticmethod
    def vibrate(duration=300):

        subprocess.run(
            [
                "termux-vibrate",
                "-d",
                str(duration)
            ]
        )

    @staticmethod
    def notify(title, message):

        subprocess.run(
            [
                "termux-notification",
                "--title",
                title,
                "--content",
                message
            ]
        )

    @staticmethod
    def clipboard():

        return Device._run(
            ["termux-clipboard-get"]
        )

    @staticmethod
    def copy(text):

        subprocess.run(
            [
                "termux-clipboard-set",
                text
            ]
        )
