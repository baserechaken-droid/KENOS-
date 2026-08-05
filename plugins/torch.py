NAME = "torch"

DESCRIPTION = "Control flashlight"

SKILLS = [
    "torch",
    "flashlight",
    "flash",
    "light",
    "lamp"
]


def run(args):

    import subprocess

    if not args:

        message = "Usage: torch on or torch off"

        print(message)

        return message

    command = " ".join(args).lower()

    try:

        if "on" in command:

            subprocess.run(
                ["termux-torch", "on"],
                check=False
            )

            message = "🔦 Flashlight ON"

            print(message)

            return message

        if "off" in command:

            subprocess.run(
                ["termux-torch", "off"],
                check=False
            )

            message = "🔦 Flashlight OFF"

            print(message)

            return message

        message = "Use: torch on or torch off"

        print(message)

        return message

    except FileNotFoundError:

        message = (
            "Termux API is not installed.\n"
            "Run: pkg install termux-api"
        )

        print(message)

        return message
