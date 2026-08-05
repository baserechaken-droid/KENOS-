import os
import importlib
import traceback

from command_manager import register, clear

loaded_plugins = {}
loaded_skills = {}

DEBUG = os.getenv("KENOS_DEBUG", "0") == "1"


def debug(message):

    if DEBUG:
        print(message)


def load_plugins():

    global loaded_plugins
    global loaded_skills

    loaded_plugins.clear()
    loaded_skills.clear()

    clear()

    plugin_dir = "plugins"

    if not os.path.isdir(plugin_dir):
        print("[ERROR] plugins directory not found.")
        return loaded_plugins

    for filename in sorted(os.listdir(plugin_dir)):

        if not filename.endswith(".py"):
            continue

        if filename.startswith("_"):
            continue

        module_name = filename[:-3]

        try:

            module = importlib.import_module(
                f"plugins.{module_name}"
            )

            module = importlib.reload(module)

            loaded_plugins[module_name] = module

            register(module_name, module)

            skills = getattr(module, "SKILLS", [])

            if isinstance(skills, (list, tuple)):

                for skill in skills:

                    if isinstance(skill, str):

                        loaded_skills[
                            skill.lower().strip()
                        ] = module_name

            debug(f"✓ Loaded {module_name}")

        except Exception as e:

            print(f"[ERROR] Failed to load {module_name}")
            print(e)

            if DEBUG:
                traceback.print_exc()

    return loaded_plugins


def get_plugin(name):

    return loaded_plugins.get(name)


def plugin_exists(name):

    return name in loaded_plugins


def get_plugins():

    return loaded_plugins


def get_skills():

    return loaded_skills


def find_skill(text):

    text = text.lower()

    for keyword, plugin in loaded_skills.items():

        if keyword in text:

            return plugin

    return None


def reload_plugin(name):

    if name not in loaded_plugins:
        return False

    try:

        module = importlib.reload(
            loaded_plugins[name]
        )

        loaded_plugins[name] = module

        register(name, module)

        debug(f"✓ Reloaded {name}")

        return True

    except Exception:

        if DEBUG:
            traceback.print_exc()

        return False


def reload_all():

    return load_plugins()
