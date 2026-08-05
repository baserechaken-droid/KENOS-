from core.planner import split_tasks


class Jarvis:


    def __init__(self):

        self.context = {
            "plugin": None,
            "args": []
        }



    def set_context(self, plugin, args):

        self.context = {
            "plugin": plugin,
            "args": args
        }



    def plan(self, text):

        tasks = split_tasks(text)

        output = []

        for task in tasks:

            if "plugin" in task:

                output.append(task)

            elif "text" in task:

                output.append(
                    {
                        "plugin": task["text"],
                        "args": [],
                        "delay": task.get(
                            "delay",
                            0
                        )
                    }
                )


        return output



    def reply(self, text):

        tasks = self.plan(text)


        if len(tasks) > 1:

            return (
                "__multi__",
                tasks
            )


        if len(tasks) == 1:

            task = tasks[0]

            return (
                task.get("plugin"),
                task.get("args", [])
            )


        return (
            None,
            []
        )



jarvis = Jarvis()
