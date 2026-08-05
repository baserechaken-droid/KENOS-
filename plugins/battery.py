NAME = "battery"

DESCRIPTION = "Show battery status"

SKILLS = [
    "battery",
    "charge",
    "power",
    "energy",
    "percentage"
]


def run(args):

    import subprocess
    import json
    import os

    message = None

    # Method 1: Termux API
    try:

        result = subprocess.run(
            ["termux-battery-status"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:

            data = json.loads(result.stdout)

            level = data.get("percentage", "Unknown")
            status = data.get("status", "Unknown")

            message = (
                f"🔋 Battery: {level}%\n"
                f"⚡ Status: {status}"
            )

            print(message)

            return message

    except Exception:
        pass

    # Method 2: Android battery path
    paths = [
        "/sys/class/power_supply/battery/capacity",
        "/sys/class/power_supply/BAT0/capacity"
    ]

    for path in paths:

        if os.path.exists(path):

            with open(path) as f:

                level = f.read().strip()

            message = f"🔋 Battery: {level}%"

            print(message)

            return message

    message = (
        "⚠️ Battery information unavailable\n"
        "Install Termux API:\n"
        "pkg install termux-api"
    )

    print(message)

    return message
