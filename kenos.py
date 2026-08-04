from plugin_loader import load_plugins, get_skills
from core.router import process
from core.diagnostics import startup_check
from core.service_manager import register, start
from core.logger import info
from services.scheduler import run as scheduler
from services.notification_service import run as notification

VERSION = "9.2 AI Edition"


def banner():

    print()
    print("=" * 46)
    print(f"          KenOS {VERSION}")
    print("=" * 46)
    print()


def startup():

    banner()

    startup_check()

    load_plugins()

    print(f"🧠 AI Skills Registered: {len(get_skills())}")

    register("scheduler", scheduler)
    register("notification", notification)

    start("scheduler")
    start("notification")

    print()
    print("🤖 Jarvis Online")
    print()
    print("Type 'help' for commands.")
    print()


def main():

    startup()

    while True:

        try:

            text = input("[KenOS] $ ").strip()

            if not text:
                continue

            if text.lower() in ("exit", "quit"):

                print("Goodbye!")
                break

            info(text)

            process(text)

        except KeyboardInterrupt:

            print()
            print("Goodbye!")
            break

        except Exception as e:

            print(f"[ERROR] {e}")


if __name__ == "__main__":
    main()
