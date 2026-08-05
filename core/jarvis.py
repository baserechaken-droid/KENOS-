from core.chat import reply as chat_reply
from core.context import context
from core.intents import detect
from core.plugin_ai import best_plugin
from core.planner import split_tasks


class Jarvis:

    def set_context(self, plugin, args):

        context.remember(plugin, args)


    def plan(self, text):

        return split_tasks(text)


    def ai_route(self, text):

        #
        # Natural language intents
        #

        intent = detect(text)

        if intent:

            return intent

        #
        # AI plugin ranking
        #

        plugin = best_plugin(text)

        if plugin:

            return (
                plugin,
                []
            )

        return None


    def reply(self, text):

        text = text.strip()

        #
        # Conversation
        #

        answer = chat_reply(text)

        if answer:

            return (
                "__chat__",
                answer
            )

        #
        # Context memory
        #

        follow = context.resolve_followup(text)

        if follow:

            return follow

        #
        # AI routing
        #

        route = self.ai_route(text)

        if route:

            return route

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

                plugin = best_plugin(
                    task["text"]
                )

                if plugin:

                    return (
                        plugin,
                        []
                    )

                return (
                    task["text"],
                    []
                )

        return (
            None,
            []
        )


jarvis = Jarvis()
