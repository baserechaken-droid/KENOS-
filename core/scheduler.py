import threading
import time


class Scheduler:

    def __init__(self):

        self.jobs = []

        self.lock = threading.Lock()


    def schedule(self, delay, callback, *args, **kwargs):

        def worker():

            time.sleep(delay)

            try:

                callback(*args, **kwargs)

            finally:

                with self.lock:

                    if thread in self.jobs:

                        self.jobs.remove(thread)

        thread = threading.Thread(
            target=worker,
            daemon=True
        )

        with self.lock:

            self.jobs.append(thread)

        thread.start()

        return thread


    def running(self):

        with self.lock:

            return len(self.jobs)


scheduler = Scheduler()

