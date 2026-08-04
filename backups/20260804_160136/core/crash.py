import traceback
from datetime import datetime

LOG = "logs/crash.log"


def save(error):

    with open(LOG, "a") as f:

        f.write("=" * 60 + "\n")

        f.write(str(datetime.now()) + "\n\n")

        f.write(str(error) + "\n\n")

        f.write(traceback.format_exc())

        f.write("\n")
