import time

from core.ui import success

def loading(text):

    print(text, end="", flush=True)

    for _ in range(10):

        time.sleep(0.05)

        print("█", end="", flush=True)

    print()

def boot():

    loading("Initializing Kernel     ")

    loading("Loading AI Engine      ")

    loading("Loading Plugins        ")

    loading("Loading Services       ")

    loading("Loading Memory         ")

    success("KenOS Ready")
