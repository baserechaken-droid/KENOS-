import importlib
import os
import sys

from command_manager import register, unregister, clear
from core.logger import info, warning, error

PLUGIN_FOLDER = "plugins"

loaded_plugins = []


def _plugin_names():

    files = []

    for filename in sorted(os.listdir(PLUGIN_FOLDER)):

        if filename.endswith(".py") and not filename.startswith("__"):

            files.append(filename[:-3])

    return files


def load_plugins():

    loaded_plugins.clear()

    success = 0
    failed = 0

    for module_name in _plugin_names():

        try:

            module = importlib.import_module(
                f"{PLUGIN_FOLDER}.{module_name}"
            )

            register(module.NAME, module)

            loaded_plugins.append(module)

            success += 1

            info(f"Loaded plugin: {module.NAME}")

        except Exception as e:

            failed += 1

            error(f"{module_name}: {e}")

            print(f"[ERROR] {module_name}: {e}")

    print(f"✓ {success} plugins loaded successfully.")

    if failed:

        print(f"⚠ {failed} plugin(s) failed.")


def reload_plugin(name):

    module_path = f"{PLUGIN_FOLDER}.{name}"

    if module_path not in sys.modules:

        print(f"{name} is not loaded.")

        return

    module = sys.modules[module_path]

    unregister(module.NAME)

    module = importlib.reload(module)

    register(module.NAME, module)

    print(f"✓ Reloaded {module.NAME}")

    info(f"Reloaded plugin: {module.NAME}")


def reload_all():

    clear()

    loaded_plugins.clear()

    for module_name in list(sys.modules.keys()):

        if module_name.startswith(f"{PLUGIN_FOLDER}."):

            importlib.reload(sys.modules[module_name])

    load_plugins()

    print("✓ All plugins reloaded.")
