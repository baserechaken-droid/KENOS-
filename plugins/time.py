from datetime import datetime

NAME = "time"
DESCRIPTION = "Show the current time"

def run(args):
    print(datetime.now().strftime("%H:%M:%S"))
