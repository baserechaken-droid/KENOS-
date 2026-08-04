from datetime import datetime

LOG_FILE = "logs/kenos.log"


def log(level, message):

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    line = f"[{now}] [{level}] {message}\n"

    with open(LOG_FILE, "a") as f:
        f.write(line)


def info(message):
    log("INFO", message)


def warning(message):
    log("WARNING", message)


def error(message):
    log("ERROR", message)
