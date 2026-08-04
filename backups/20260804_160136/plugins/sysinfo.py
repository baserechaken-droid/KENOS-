import platform
import os

NAME = "sysinfo"
DESCRIPTION = "Show device information"


def run(args):

    print()

    print("========== SYSTEM ==========")

    print("System :", platform.system())
    print("Release:", platform.release())
    print("Machine:", platform.machine())
    print("Python :", platform.python_version())
    print("User   :", os.getenv("USER"))

    print()
