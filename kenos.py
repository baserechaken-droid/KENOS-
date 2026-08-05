from plugin_loader import load_plugins, get_skills
from core.router import process
from core.diagnostics import startup_check
from core.service_manager import register, start
from core.logger import info
from core.prompt import get_prompt
from core.logo import show as show_logo

from services.scheduler import run as scheduler
from services.notification_service import run as notification

import platform
from datetime import datetime


VERSION = "10 AI Edition"


def banner():

    show_logo()

    print()
    print("        Android AI Operating System")
    print(f"             Version {VERSION}")
    print()

    print("Initializing AI Engine...")
    print("[████████████████████████████████] 100%")
    print()

    print("Loading Plugins...")
    print("[████████████████████████████████] 100%")
    print()

    print("Starting Services...")
    print("[████████████████████████████████] 100%")
    print()

    print("Preparing Voice Assistant...")
    print("[████████████████████████████████] 100%")
    print()


def system_info():

    now = datetime.now()

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    print(
        f"✓ System      : Android"
    )

    print(
        f"✓ Python      : {platform.python_version()}"
    )

    print(
        f"✓ Date        : {now.strftime('%d %B %Y')}"
    )

    print(
        f"✓ Time        : {now.strftime('%H:%M:%S')}"
    )

    print(
        "✓ Status      : READY"
    )

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print()


def startup():

    banner()

    startup_check()

    load_plugins()

    print(
        f"✓ Plugins Loaded : {len(get_skills())}"
    )

    register(
        "scheduler",
        scheduler
    )

    register(
        "notification",
        notification
    )

    start("scheduler")
    start("notification")

    system_info()

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("✓ System Ready")
    print("✓ AI Engine Ready")
    print(f"✓ AI Skills      : {len(get_skills())}")
    print("✓ Voice Engine   : Ready")
    print("✓ Scheduler      : Running")
    print("✓ Notifications  : Running")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    print()

    print("🤖 Jarvis Online")

    print()

    print("Commands:")
    print("  help     - Show commands")
    print("  listen   - Single voice command")
    print("  voice    - Continuous voice mode")
    print("  exit     - Shutdown KenOS")

    print()


def main():

    startup()

    while True:

        try:

            text = input(
                get_prompt()
            ).strip()


            if not text:

                continue


            if text.lower() in (
                "exit",
                "quit",
                "shutdown"
            ):

                print()
                print("🤖 Jarvis shutting down...")
                print("Goodbye!")
                break


            info(text)

            process(text)


        except KeyboardInterrupt:

            print()
            print("🤖 Jarvis shutting down...")
            print("Goodbye!")
            break


        except Exception as e:

            print(
                f"[ERROR] {e}"
            )


if __name__ == "__main__":

    main()
