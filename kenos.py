from plugin_loader import load_plugins, get_skills, get_plugins
from core.router import process
from core.diagnostics import startup_check
from core.service_manager import register, start
from core.logger import info
from core.logo import show as logo
from core.prompt import prompt

from services.scheduler import run as scheduler
from services.notification_service import run as notification


VERSION = "10 AI Edition"


def banner():

    logo()


def dashboard():

    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print("✓ System Ready")
    print("✓ AI Engine Ready")
    print(f"✓ Plugins Loaded : {len(get_plugins())}")
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


def startup():

    banner()

    startup_check()

    plugins = load_plugins()

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

    dashboard()


def main():

    startup()

    while True:

        try:

            text = input(prompt()).strip()

            if not text:

                continue


            if text.lower() in (
                "exit",
                "quit",
                "shutdown"
            ):

                print()
                print("👋 Shutting down KenOS...")
                break


            info(text)

            process(text)


        except KeyboardInterrupt:

            print()
            print()
            print("👋 Shutting down KenOS...")
            break


        except Exception as e:

            print(f"[ERROR] {e}")


if __name__ == "__main__":

    main()
