import json
import subprocess

NAME = "battery"
DESCRIPTION = "Show battery percentage and charging status"

def run(args):
    result = subprocess.run(
        ["termux-battery-status"],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print("Error: Could not get battery information.")
        return

    data = json.loads(result.stdout)

    print("\nBattery")
    print("----------------")
    print(f"Level : {data['percentage']}%")
    print(f"Status: {data['status']}")
    print(f"Health: {data['health']}")
