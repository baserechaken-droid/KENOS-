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

        print(
            "Usage: torch on/off"
        )

        return


    command = " ".join(args).lower()


    try:

        if any(x in command for x in ["on","enable","start"]):

            subprocess.run(
                ["termux-torch","on"]
            )

            print(
                "🔦 Flashlight ON"
            )


        elif any(x in command for x in ["off","disable","stop"]):

            subprocess.run(
                ["termux-torch","off"]
            )

            print(
                "🔦 Flashlight OFF"
            )


        else:

            print(
                "Use torch on or torch off"
            )


    except FileNotFoundError:

        print(
            "⚠️ Install Termux API:"
        )

        print(
            "pkg install termux-api"
        )
