from command_manager import execute, exists
from core.jarvis import jarvis
from core.voice import speak


def run_plugin(plugin, args):

    result = execute(plugin, args)

    if isinstance(result, str) and result.strip():

        try:
            speak(result)
        except Exception:
            pass

    return result


def process(text):

    text = text.strip()

    if not text:
        return

    words = text.split()

    command = words[0].lower()

    # Direct command
    if exists(command):

        run_plugin(command, words[1:])

        return

    # AI
    plugin, args = jarvis.reply(text)

    if plugin and exists(plugin):

        print(f"🤖 Jarvis → {plugin}")

        run_plugin(plugin, args)

        return

    print("🤖 Sorry, I don't understand that command yet.")
