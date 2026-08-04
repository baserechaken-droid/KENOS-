import platform
import os

NAME = "system"
DESCRIPTION = "Display system information"


def run(args):

    print()

    print("========== SYSTEM ==========")

    print("OS       :", platform.system())

    print("Release  :", platform.release())

    print("Python   :", platform.python_version())

    print("CPU      :", os.cpu_count())

    print()
