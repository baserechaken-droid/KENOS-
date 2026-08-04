from plugin_loader import find_skill
from command_manager import execute, exists
from core.jarvis import jarvis


def process(text):

    text = text.strip()

    if not text:
        return

    words = text.split()

    command = words[0].lower()

    # Direct command
    if exists(command):

        execute(command, words[1:])

        return

    # AI Skill Router
    plugin = find_skill(text)

    if plugin:

        print(f"🤖 Skill Router → {plugin}")

        args = words[:]

        if args and args[0].lower() == plugin:
            args = args[1:]

        execute(plugin, args)

        return

    # Jarvis fallback
    try:

        plugin, args = jarvis.reply(text)

        if plugin and exists(plugin):

            print(f"🤖 Jarvis → {plugin}")

            execute(plugin, args)

            return

    except Exception:
        pass

    print("🤖 Sorry, I don't understand that command yet.")
