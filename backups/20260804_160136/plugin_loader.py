import os
import importlib

from command_manager import register

PLUGIN_FOLDER = "plugins"

loaded_plugins = []


def load_plugins():

    global loaded_plugins

    loaded_plugins = []

    for file in sorted(os.listdir(PLUGIN_FOLDER)):

        if not file.endswith(".py"):
            continue

        if file == "__init__.py":
            continue

        module_name = file[:-3]

        try:

            module = importlib.import_module(
                f"{PLUGIN_FOLDER}.{module_name}"
            )

            register(module.NAME, module.run)

            loaded_plugins.append(module)

        except Exception as e:

            print(f"[ERROR] {module_name}: {e}")

    return loaded_plugins
