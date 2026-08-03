import os
import importlib

from command_manager import register

PLUGIN_FOLDER = "plugins"

loaded_plugins = []

def load_plugins():
    global loaded_plugins

    for file in os.listdir(PLUGIN_FOLDER):

        if file.endswith(".py") and file != "__init__.py":

            module_name = file[:-3]

            module = importlib.import_module(
                f"{PLUGIN_FOLDER}.{module_name}"
            )

            register(module.NAME, module.run)

            loaded_plugins.append(module)

    return loaded_plugins
