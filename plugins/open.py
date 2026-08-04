import subprocess

NAME = "open"
DESCRIPTION = "Open apps, Android settings, websites and searches"


SETTINGS = {
    "settings": "android.settings.SETTINGS",
    "wifi": "android.settings.WIFI_SETTINGS",
    "bluetooth": "android.settings.BLUETOOTH_SETTINGS",
    "display": "android.settings.DISPLAY_SETTINGS",
    "sound": "android.settings.SOUND_SETTINGS",
    "battery": "android.settings.BATTERY_SAVER_SETTINGS",
    "location": "android.settings.LOCATION_SOURCE_SETTINGS",
    "security": "android.settings.SECURITY_SETTINGS",
    "apps": "android.settings.APPLICATION_SETTINGS",
    "storage": "android.settings.INTERNAL_STORAGE_SETTINGS",
    "accessibility": "android.settings.ACCESSIBILITY_SETTINGS",
    "developer": "android.settings.APPLICATION_DEVELOPMENT_SETTINGS",
    "about": "android.settings.DEVICE_INFO_SETTINGS"
}


URLS = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "gmail": "https://mail.google.com",
    "maps": "https://maps.google.com",
    "drive": "https://drive.google.com",
    "github": "https://github.com",
    "chatgpt": "https://chat.openai.com"
}


def open_url(url):
    subprocess.run(["termux-open-url", url])


def start_action(action):
    subprocess.run([
        "am",
        "start",
        "-a",
        action
    ])


def start_camera():
    start_action("android.media.action.IMAGE_CAPTURE")


def start_dialer():
    start_action("android.intent.action.DIAL")


def run(args):

    if not args:
        print("Usage: open <target>")
        return

    target = " ".join(args).strip()
    lower = target.lower()

    # Android Settings
    if lower in SETTINGS:
        start_action(SETTINGS[lower])
        return

    # Camera
    if lower == "camera":
        start_camera()
        return

    # Phone
    if lower in ("phone", "dialer"):
        start_dialer()
        return

    # Common websites
    if lower in URLS:
        open_url(URLS[lower])
        return

    # URLs
    if lower.startswith("http://") or lower.startswith("https://"):
        open_url(target)
        return

    if lower.startswith("www."):
        open_url("https://" + target)
        return

    # Google search
    if lower.startswith("search "):
        query = target[7:].strip().replace(" ", "+")
        open_url(f"https://www.google.com/search?q={query}")
        return

    # YouTube search
    if lower.startswith("youtube "):
        query = target[8:].strip().replace(" ", "+")
        open_url(f"https://www.youtube.com/results?search_query={query}")
        return

    # Maps search
    if lower.startswith("map "):
        query = target[4:].strip().replace(" ", "+")
        open_url(f"https://www.google.com/maps/search/{query}")
        return

    # Default: Google search
    open_url(
        "https://www.google.com/search?q=" +
        target.replace(" ", "+")
    )
