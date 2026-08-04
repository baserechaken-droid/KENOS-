import threading
import time

_tasks = []


def schedule(delay, func, *args):

    def wrapper():
        time.sleep(delay)

        try:
            func(*args)
        except Exception as e:
            print(f"[Scheduler] {e}")

    thread = threading.Thread(
        target=wrapper,
        daemon=True
    )

    thread.start()

    _tasks.append({
        "delay": delay,
        "function": func.__name__
    })


def tasks():
    return list(_tasks)
