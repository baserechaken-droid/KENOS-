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
            voice.speak(
                str(text)
            )

    except:

        pass



def run_plugin(plugin, args):

    jarvis.set_context(
        plugin,
        args
    )


    result = execute(
        plugin,
        args
    )


    if isinstance(result, str) and result.strip():

        print(
            "🤖 Jarvis:",
            result
        )

        speak(
            result
        )


    return result



def run_plan(plan):

    for step in plan:

        delay = step.get(
            "delay",
            0
        )


        if delay > 0:

            print(
                f"⏳ Waiting {delay} second(s)..."
            )

            time.sleep(delay)


        plugin = step.get(
            "plugin"
        )

        args = step.get(
            "args",
            []
        )


        print(
            f"🤖 Jarvis → {plugin}"
        )


        run_plugin(
            plugin,
            args
        )



def process(text):

    text = text.strip()


    if not text:
        return



    words = text.split()

    command = words[0].lower()



    if exists(command) and len(words) == 1:

        run_plugin(
            command,
            []
        )

        return



    plugin, data = jarvis.reply(text)



    if plugin == "__multi__":

        print(
            "🧠 Planning..."
        )

        run_plan(
            data
        )

        return



    if plugin:

        run_plugin(
            plugin,
            data
        )

        return



    if exists(command):

        run_plugin(
            command,
            words[1:]
        )

        return



    message = (
        "Sorry Ken, I did not understand that command."
    )

    print(
        "🤖 Jarvis:",
        message
    )

    speak(
        message
    )
