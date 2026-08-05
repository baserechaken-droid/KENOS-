import time

from command_manager import execute, exists
from core.jarvis import jarvis
from core.voice import speak


def run_plugin(plugin, args):

    jarvis.set_context(plugin, args)

    result = execute(plugin, args)

    if isinstance(result, str) and result.strip():

        try:
            speak(result)
        except Exception:
            pass

    return result


def run_plan(plan):

    for step in plan:

        delay = step.get("delay", 0)

        if delay > 0:

            print(f"⏳ Waiting {delay} second(s)...")

            time.sleep(delay)

        plugin = step["plugin"]
        args = step["args"]

        print(f"🤖 Jarvis → {plugin}")

        run_plugin(plugin, args)


def process(text):

    text = text.strip()

    if not text:
        return

    #
    # Direct command only if the FIRST WORD is an actual command.
    #

    words = text.split()

    command = words[0].lower()

    if exists(command) and len(words) == 1:

        run_plugin(command, [])

        return

    #
    # AI
    #

    plugin, data = jarvis.reply(text)

    if plugin == "__multi__":

        print("🧠 Planning...")

        run_plan(data)

        return

    if plugin:

        run_plugin(plugin, data)

        return

    #
    # Fallback direct command with arguments.
    #

    if exists(command):

        run_plugin(command, words[1:])

        return

    print("🤖 Sorry, I don't understand that command yet.")

    try:
        speak("Sorry, I don't understand that command yet.")
    except Exception:
        pass
