from core.plugin_ai import best_plugin
from core.parser import parse


class ActionEngine:

    def decide(self, text):

        plugin = best_plugin(text)

        if not plugin:

            return None

        args = parse(
            plugin,
            text
        )

        return {
            "plugin": plugin,
            "args": args,
            "confidence": 1.0
        }


engine = ActionEngine()

