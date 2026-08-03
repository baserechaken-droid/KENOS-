from datetime import datetime

NAME = "date"
DESCRIPTION = "Show today's date"

def run(args):
    print(datetime.now().strftime("%d %B %Y"))
