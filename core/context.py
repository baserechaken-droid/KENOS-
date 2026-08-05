from datetime import datetime


class Context:

    def __init__(self):

        self.reset()


    def reset(self):

        self.plugin = None

        self.args = []

        self.time = None

        self.history = []


    def remember(self, plugin, args):

        self.plugin = plugin

        self.args = list(args)

        self.time = datetime.now()

        self.history.append(
            {
                "plugin": plugin,
                "args": list(args),
                "time": self.time
            }
        )

        if len(self.history) > 50:

            self.history.pop(0)


    def last_plugin(self):

        return self.plugin


    def last_args(self):

        return self.args


    def resolve_followup(self, text):

        text = text.lower()

        #
        # Torch context
        #

        if self.plugin == "torch":

            if any(
                x in text for x in (
                    "turn it off",
                    "switch it off",
                    "disable it",
                    "turn off",
                    "switch off"
                )
            ):

                return (
                    "torch",
                    ["off"]
                )

            if any(
                x in text for x in (
                    "turn it on",
                    "switch it on",
                    "enable it",
                    "turn on",
                    "switch on"
                )
            ):

                return (
                    "torch",
                    ["on"]
                )

        #
        # Repeat last command
        #

        if any(
            x in text for x in (
                "again",
                "repeat",
                "do that again",
                "repeat that"
            )
        ):

            if self.plugin:

                return (
                    self.plugin,
                    self.args
                )

        return None


context = Context()

