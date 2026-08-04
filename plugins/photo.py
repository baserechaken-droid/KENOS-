import subprocess
import os

NAME = "photo"
DESCRIPTION = "Take a photo"

def run(args):

    filename = os.path.expanduser(
        "~/storage/downloads/photo.jpg"
    )

    subprocess.run([
        "termux-camera-photo",
        filename
    ])

    print("Saved:", filename)
