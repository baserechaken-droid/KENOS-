import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "kenos.log")

LEVEL_INFO = "INFO"
LEVEL_WARNING = "WARNING"
LEVEL_ERROR = "ERROR"
LEVEL_DEBUG = "DEBUG"


def _ensure():

    os.makedirs(LOG_DIR, exist_ok=True)


def _write(level, message):

    _ensure()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line = f"[{timestamp}] [{level}] {message}"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

    print(line)


def info(message):

    _write(LEVEL_INFO, message)


def warning(message):

    _write(LEVEL_WARNING, message)


def error(message):

    _write(LEVEL_ERROR, message)


def debug(message):

    _write(LEVEL_DEBUG, message)


def clear():

    _ensure()

    open(LOG_FILE, "w", encoding="utf-8").close()


def tail(lines=20):

    _ensure()

    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return f.readlines()[-lines:]


def logfile():

    return LOG_FILE
