import json
import os
import threading
import time
import uuid

FILE = "data/scheduler.json"


class Scheduler:

    def __init__(self):

        self.jobs = {}

        self.lock = threading.Lock()

        os.makedirs("data", exist_ok=True)

        self._save()


    def _save(self):

        data = {}

        with self.lock:

            for job_id, job in self.jobs.items():

                data[job_id] = {
                    "message": job["message"],
                    "run_at": job["run_at"]
                }

        with open(FILE, "w") as f:

            json.dump(
                data,
                f,
                indent=4
            )


    def schedule(self, delay, callback, *args, message="Task", **kwargs):

        job_id = str(uuid.uuid4())[:8]

        run_at = time.time() + delay

        def worker():

            time.sleep(delay)

            try:

                callback(*args, **kwargs)

            finally:

                with self.lock:

                    self.jobs.pop(job_id, None)

                self._save()

        thread = threading.Thread(
            target=worker,
            daemon=True
        )

        with self.lock:

            self.jobs[job_id] = {
                "thread": thread,
                "message": message,
                "run_at": run_at
            }

        self._save()

        thread.start()

        return job_id


    def list_jobs(self):

        output = []

        with self.lock:

            now = time.time()

            for job_id, job in self.jobs.items():

                output.append(
                    {
                        "id": job_id,
                        "message": job["message"],
                        "remaining": max(
                            0,
                            int(job["run_at"] - now)
                        )
                    }
                )

        return output


    def cancel(self, job_id):

        with self.lock:

            if job_id not in self.jobs:

                return False

            self.jobs.pop(job_id)

        self._save()

        return True


    def running(self):

        with self.lock:

            return len(self.jobs)


scheduler = Scheduler()

