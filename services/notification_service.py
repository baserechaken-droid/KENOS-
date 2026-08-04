import subprocess
import queue
import threading

_notifications = queue.Queue()


def notify(title, content):

    _notifications.put((title, content))


def worker():

    while True:

        title, content = _notifications.get()

        try:

            subprocess.run([
                "termux-notification",
                "--title", title,
                "--content", content
            ])

        except Exception as e:
            print("[Notification]", e)


def run():

    thread = threading.Thread(
        target=worker,
        daemon=True
    )

    thread.start()
