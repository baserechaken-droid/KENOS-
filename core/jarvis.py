from core.chat import reply as chat_reply
from core.context import context
from core.intents import detect
from core.planner import split_tasks


class Jarvis:

    def set_context(self, plugin, args):

        context.remember(plugin, args)

    def plan(self, text):

        return split_tasks(text)

    def reply(self, text):

        #
        # Chat responses
        #

        answer = chat_reply(text)

        if answer:

            return (
                "__chat__",
                answer
            )

        #
        # Context follow-up
        #

        follow = context.resolve_followup(text)

        if follow:

            return follow

        #
        # Intent detection
        #

        intent = detect(text)

        if intent:

            return intent

        #
        # Planner
        #

        tasks = self.plan(text)

        if len(tasks) > 1:

            return (
                "__multi__",
                tasks
            )

        if len(tasks) == 1:

            task = tasks[0]

            if "plugin" in task:

                return (
                    task["plugin"],
                    task.get(
                        "args",
                        []
                    )
                )

            if "text" in task:

                return (
                    task["text"],
                    []
                )

        return (
            None,
            []
        )


jarvis = Jarvis()

