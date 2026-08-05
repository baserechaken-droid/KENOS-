import time

from command_manager import execute, exists
from core.jarvis import jarvis

try:
    from services.voice.engine import voice
except Exception:
    voice = None


def speak(text):

    if not text:
        return

    try:
        if voice:
            voice.speak(str(text))
    except Exception:
        pass


def run_plugin(plugin, args):

    if hasattr(jarvis, "set_context"):

        try:
            jarvis.set_context(plugin, args)
        except Exception:
            pass

    result = execute(plugin, args)

    if isinstance(result, str) and result.strip():

        print(f"🤖 Jarvis: {result}")

        speak(result)

    return result


def run_plan(plan):

    if not isinstance(plan, list):
        return

    for step in plan:

        if not isinstance(step, dict):
            continue

        plugin = step.get("plugin")

        if not plugin:
            continue

        args = step.get("args", [])
        delay = step.get("delay", 0)

        print(f"🤖 Jarvis → {plugin}")

        run_plugin(plugin, args)

        if delay > 0:

            print(f"⏳ Waiting {delay} second(s)...")

            time.sleep(delay)


def process(text):

    text = text.strip()

    if not text:
        return

    words = text.split()

    command = words[0].lower()

    #
    # Execute registered plugins FIRST.
    #

    if exists(command):

        run_plugin(command, words[1:])

        return

    #
    # AI processing.
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
    # Unknown command.
    #

    message = "Sorry Ken, I did not understand that command."

    print(f"🤖 Jarvis: {message}")

    speak(message)
