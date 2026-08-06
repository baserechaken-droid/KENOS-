from plugin_loader import get_plugins


class PluginRegistry:

    def __init__(self):

        self.refresh()


    def refresh(self):

        self.plugins = {}

        for name, module in get_plugins().items():

            self.plugins[name] = {

                "name": name,

                "description": getattr(
                    module,
                    "DESCRIPTION",
                    ""
                ),

                "skills": getattr(
                    module,
                    "SKILLS",
                    []
                ),

                "module": module
            }


    def names(self):

        return sorted(self.plugins.keys())


    def exists(self, name):

        return name in self.plugins


    def get(self, name):

        return self.plugins.get(name)


    def search(self, keyword):

        keyword = keyword.lower()

        results = []

        for plugin in self.plugins.values():

            if keyword in plugin["name"].lower():

                results.append(plugin)

                continue

            if keyword in plugin["description"].lower():

                results.append(plugin)

                continue

            for skill in plugin["skills"]:

                if keyword in skill.lower():

                    results.append(plugin)

                    break

        return results


registry = PluginRegistry()

