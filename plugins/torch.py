NAME = "torch"

DESCRIPTION = "Control flashlight"

SKILLS = [
    "torch",
    "flashlight",
    "light",
    "lamp"
]


def run(args):

    import subprocess

    if not args:

        print("Usage: torch on/off")
        return "Say torch on or torch off."

    command = " ".join(args).lower()

    try:

        if "on" in command:

            subprocess.run(
                ["termux-torch", "on"],
                check=False
            )

            print("🔦 Flashlight ON")

            return "Flashlight turned on."

        if "off" in command:

            subprocess.run(
                ["termux-torch", "off"],
                check=False
            )

            print("🔦 Flashlight OFF")

            return "Flashlight turned off."

        print("Use torch on or torch off")

        return "Please say on or off."

    except FileNotFoundError:

        print("⚠️ Install Termux API:")
        print("pkg install termux-api")

        return "Termux API is not installed."
