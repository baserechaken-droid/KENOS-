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

    jarvis.set_context(plugin, args)

    result = execute(plugin, args)

    if isinstance(result, str) and result.strip():

        print(f"🤖 Jarvis: {result}")

        speak(result)

    return result


def run_plan(plan):

    for step in plan:

        delay = step.get("delay", 0)

        if delay > 0:

            print(f"⏳ Waiting {delay} second(s)...")

            time.sleep(delay)

        plugin = step.get("plugin")

        if not plugin:

            continue

        args = step.get("args", [])

        print(f"🤖 Jarvis → {plugin}")

        run_plugin(plugin, args)


def process(text):

    text = text.strip()

    if not text:
        return

    #
    # Direct command
    #

    words = text.split()

    command = words[0].lower()

    if exists(command):

        run_plugin(
            command,
            words[1:]
        )

        return

    #
    # AI
    #

    plugin, data = jarvis.reply(text)

    if plugin == "__chat__":

        print(f"🤖 Jarvis: {data}")

        speak(data)

        return

    if plugin == "__multi__":

        print("🧠 Planning...")

        run_plan(data)

        return

    if plugin:

        run_plugin(plugin, data)

        return

    #
    # Unknown
    #

    message = "Sorry Ken, I didn't understand that."

    print(f"🤖 Jarvis: {message}")

    speak(message)

