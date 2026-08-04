from core.jarvis import jarvis
from core.skills import detect_intent
from command_manager import execute, exists



def process(text):

    words = text.strip().split()


    if not words:
        return



    command = words[0].lower()


    # Direct commands

    if exists(command):

        execute(command, words[1:])

        return



    # AI skill detection

    intent = detect_intent(text)


    if intent and exists(intent):

        print(f"🤖 Skill → {intent}")

        execute(intent, words[1:])

        return



    # Jarvis reasoning

    plugin, args = jarvis.reply(text)


    if plugin:

        print(f"🤖 Jarvis → {plugin}")

        execute(plugin,args)

        return



    print(
        "🤖 Sorry, I don't understand that yet."
    )
