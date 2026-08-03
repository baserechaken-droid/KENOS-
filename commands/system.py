import os

def battery():
    os.system("termux-battery-status")

def torch(state):
    os.system(f"termux-torch {state}")
