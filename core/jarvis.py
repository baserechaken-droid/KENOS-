from core.nlp import parse
from core.memory import remember as save_memory
from core.memory import recall as load_memory
from core.planner import split_tasks


class Jarvis:

    def __init__(self):

        self.session = {
            "history": [],
            "last_plugin": None,
            "last_args": []
        }

    #
    # Conversation Context
    #

    def set_context(self, plugin, args=None):

        self.session["last_plugin"] = plugin
        self.session["last_args"] = list(args or [])

    def get_context(self):

        return (
            self.session["last_plugin"],
            self.session["last_args"]
        )

    #
    # Planner
    #

    def plan(self, text):

        plan = []

        current_plugin = None
        current_args = []

        for task in split_tasks(text):

            task_text = task["text"].strip()

            delay = task["delay"]

            intent = parse(task_text)

            #
            # Normal command
            #

            if intent.command:

                current_plugin = intent.command
                current_args = list(intent.args)

                plan.append({

                    "plugin": current_plugin,

                    "args": current_args,

                    "delay": delay

                })

                continue

            #
            # Context-aware planning
            #

            words = task_text.lower().split()

            if current_plugin:

                if "again" in words:

                    plan.append({

                        "plugin": current_plugin,

                        "args": current_args,

                        "delay": delay

                    })

                    continue

            if current_plugin == "torch":

                if "off" in words:

                    current_args = ["off"]

                    plan.append({

                        "plugin": "torch",

                        "args": ["off"],

                        "delay": delay

                    })

                    continue

                if "on" in words:

                    current_args = ["on"]

                    plan.append({

                        "plugin": "torch",

                        "args": ["on"],

                        "delay": delay

                    })

                    continue

        return plan

    #
    # AI Reply
    #

    def reply(self, text):

        text = text.strip()

        if not text:

            return None, None

        self.session["history"].append(text)

        #
        # Multi-command planning
        #

        plan = self.plan(text)

        if len(plan) > 1:

            if plan:

                last = plan[-1]

                self.set_context(
                    last["plugin"],
                    last["args"]
                )

            return "__multi__", plan

        if len(plan) == 1:

            step = plan[0]

            self.set_context(
                step["plugin"],
                step["args"]
            )

            return step["plugin"], step["args"]

        #
        # Conversation Context
        #

        words = text.lower().split()

        plugin, args = self.get_context()

        if plugin:

            if "again" in words:

                return plugin, args

            if plugin == "torch":

                if "off" in words:

                    self.set_context(
                        "torch",
                        ["off"]
                    )

                    return "torch", ["off"]

                if "on" in words:

                    self.set_context(
                        "torch",
                        ["on"]
                    )

                    return "torch", ["on"]

        return None, None

    #
    # Memory
    #

    def remember(self, key, value):

        save_memory(key, value)

    def recall(self, key):

        return load_memory(key)

    #
    # History
    #

    def last(self):

        history = self.session["history"]

        if not history:

            return None

        return history[-1]

    def clear(self):

        self.session = {

            "history": [],

            "last_plugin": None,

            "last_args": []

        }


jarvis = Jarvis()
