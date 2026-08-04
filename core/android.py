import subprocess


class Android:

    @staticmethod
    def run(command):

        try:

            subprocess.run(command)

            return True

        except Exception:

            return False


    @staticmethod
    def torch(on):

        return Android.run([
            "termux-torch",
            "on" if on else "off"
        ])


    @staticmethod
    def speak(text):

        return Android.run([
            "termux-tts-speak",
            text
        ])


    @staticmethod
    def vibrate(ms=300):

        return Android.run([
            "termux-vibrate",
            "-d",
            str(ms)
        ])


    @staticmethod
    def notify(title, message):

        return Android.run([
            "termux-notification",
            "--title",
            title,
            "--content",
            message
        ])


    @staticmethod
    def open(target):

        return Android.run([
            "termux-open",
            target
        ])
