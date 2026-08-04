import os
import platform

NAME = "sysinfo"
DESCRIPTION = "Display KenOS system information"


def run(args):

    print()

    print("=" * 40)
    print("KENOS SYSTEM INFORMATION")
    print("=" * 40)

    print("KenOS Version :", "8.0 Stable")
    print("Python        :", platform.python_version())
    print("Platform      :", platform.system())
    print("Architecture  :", platform.machine())
    print("Working Dir   :", os.getcwd())

    print()
