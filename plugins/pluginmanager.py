import os

NAME = "pluginmanager"
DESCRIPTION = "Manage KenOS plugins"


PLUGIN_DIR = "plugins"


def plugin_list():

    plugins = []

    for file in sorted(os.listdir(PLUGIN_DIR)):

        if file.endswith(".py") and not file.startswith("__"):

            plugins.append(file[:-3])

    return plugins


def run(args):

    if not args:

        print()
        print("KenOS Plugin Manager")
        print("--------------------")
        print("list")
        print("count")
        print("info <plugin>")
        print()

        return


    command = args[0].lower()


    if command == "list":

        print()

        print("Installed Plugins")

        print("-----------------")

        for plugin in plugin_list():

            print("✓", plugin)

        print()

        return


    if command == "count":

        print()

        print(
            f"Installed Plugins: {len(plugin_list())}"
        )

        print()

        return


    if command == "info":

        if len(args) < 2:

            print("Usage: pluginmanager info <plugin>")

            return


        plugin = args[1]

        path = os.path.join(
            PLUGIN_DIR,
            plugin + ".py"
        )


        if not os.path.exists(path):

            print("Plugin not found.")

            return


        print()

        print("Plugin :", plugin)

        print("File   :", path)

        print(
            "Size   :",
            os.path.getsize(path),
            "bytes"
        )

        print()

        return


    print("Unknown command.")
