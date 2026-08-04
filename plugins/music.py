import subprocess

NAME = "music"
DESCRIPTION = "Control media playback"

def run(args):

    if not args:
        print("Usage:")
        print("music play")
        print("music pause")
        print("music stop")
        print("music info")
        return

    cmd = args[0].lower()

    if cmd == "play":
        subprocess.run(["termux-media-player", "play"])
        print("▶ Playing")

    elif cmd == "pause":
        subprocess.run(["termux-media-player", "pause"])
        print("⏸ Paused")

    elif cmd == "stop":
        subprocess.run(["termux-media-player", "stop"])
        print("⏹ Stopped")

    elif cmd == "info":
        subprocess.run(["termux-media-player", "info"])

    else:
        print("Unknown command")
