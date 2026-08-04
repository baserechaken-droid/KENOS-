import os

NAME = "update"
DESCRIPTION = "Check project version"


def run(args):

    print()

    print("KenOS Version")

    print("----------------")

    if os.path.exists(".git"):

        print("Git repository detected.")

        print("Use:")

        print("git pull")

    else:

        print("Not a Git repository.")

    print()
