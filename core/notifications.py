from datetime import datetime

try:
    from services.voice.engine import voice
except Exception:
    voice = None


class NotificationCenter:

    def __init__(self):

        self.history = []


    def notify(self, title, message, speak=True):

        item = {
            "time": datetime.now().strftime("%H:%M:%S"),
            "title": title,
            "message": message
        }

        self.history.append(item)

        print()
        print(f"🔔 {title}")
        print("-" * 40)
        print(message)
        print()

        if speak and voice:

            try:
                voice.speak(message)
            except Exception:
                pass


    def recent(self, limit=10):

        return self.history[-limit:]


    def clear(self):

        self.history.clear()


notifications = NotificationCenter()

