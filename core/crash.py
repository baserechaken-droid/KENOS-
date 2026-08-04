import os
import traceback
from datetime import datetime

CRASH_DIR = "logs"
CRASH_FILE = os.path.join(CRASH_DIR, "crashes.log")


def _ensure():

    os.makedirs(CRASH_DIR, exist_ok=True)


def report(exc):

    _ensure()

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(CRASH_FILE, "a", encoding="utf-8") as f:

        f.write("=" * 70 + "\n")
        f.write(f"Time: {now}\n")
        f.write(traceback.format_exc())
        f.write("\n")


def read():

    _ensure()

    if not os.path.exists(CRASH_FILE):
        return ""

    with open(CRASH_FILE, "r", encoding="utf-8") as f:
        return f.read()


def clear():

    _ensure()

    open(CRASH_FILE, "w", encoding="utf-8").close()
