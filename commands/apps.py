import subprocess
import os

APPS = {
    "whatsapp": "com.whatsapp",
    "youtube": "com.google.android.youtube",
    "chrome": "com.android.chrome",
    "settings": "android.settings.SETTINGS",
}

def list_apps():
    try:
        result = subprocess.run(
            ["cmd", "package", "list", "packages"],
            capture_output=True,
            text=True
        )

        for line in result.stdout.splitlines():
            print(line.replace("package:", ""))

    except Exception as e:
        print("Error:", e)

def open_app(name):
    name = name.lower()

    if name == "settings":
        os.system("am start -a android.settings.SETTINGS")
        return

    if name in APPS:
        print(f"Opening {name}...")
        os.system(f"am start -p {APPS[name]}")
    else:
        print("Unknown app.")
