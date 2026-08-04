import platform

NAME = "version"
DESCRIPTION = "Display KenOS version"


VERSION = "8.0.0"


def run(args):

    print()

    print("KenOS Version")

    print("------------------------")

    print("Version :", VERSION)

    print("Python  :", platform.python_version())

    print("Platform:", platform.system())

    print()
