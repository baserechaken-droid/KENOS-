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

    # Method 1: Termux API
    try:

        result = subprocess.run(
            ["termux-battery-status"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:

            data = json.loads(result.stdout)

            percentage = data.get("percentage", "Unknown")
            status = data.get("status", "Unknown")

            print(f"🔋 Battery: {percentage}%")
            print(f"⚡ Status: {status}")

            return f"Battery is {percentage} percent and {status.lower()}."

    except Exception:
        pass

    # Method 2: Android battery sysfs
    paths = [
        "/sys/class/power_supply/battery/capacity",
        "/sys/class/power_supply/BAT0/capacity"
    ]

    for path in paths:

        if os.path.exists(path):

            with open(path) as f:
                level = f.read().strip()

            print(f"🔋 Battery: {level}%")

            return f"Battery is {level} percent."

    print("⚠️ Battery information unavailable")
    print("Install Termux API:")
    print("pkg install termux-api")

    return "Battery information is unavailable."
