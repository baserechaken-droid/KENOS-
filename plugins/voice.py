from services.voice.engine import voice


NAME = "voice"
DESCRIPTION = "Control Jarvis voice"



def run(args):

    if not args:

        print(voice.status())
        return


    command = args[0]


    if command == "test":

        voice.speak(
            "Hello Ken. Jarvis voice engine is online."
        )

        print(
            "🔊 Voice test completed"
        )


    elif command == "on":

        voice.settings["enabled"] = True
        print(
            "🔊 Jarvis voice enabled"
        )


    elif command == "off":

        voice.settings["enabled"] = False
        print(
            "🔇 Jarvis voice disabled"
        )


    else:

        print(
            "voice commands: test, on, off"
        )
