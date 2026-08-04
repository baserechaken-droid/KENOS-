import os
import importlib


loaded_skills = {}


def load_skills():

    global loaded_skills

    loaded_skills = {}


    plugin_folder = "plugins"


    for file in os.listdir(plugin_folder):

        if not file.endswith(".py"):
            continue


        if file == "__init__.py":
            continue


        plugin_name = file[:-3]


        try:

            module = importlib.import_module(
                f"plugins.{plugin_name}"
            )


            if hasattr(module, "SKILLS"):

                for skill in module.SKILLS:

                    loaded_skills[
                        skill.lower()
                    ] = plugin_name



        except Exception as e:

            print(
                f"[Skill Loader Error] {plugin_name}: {e}"
            )


    return loaded_skills



def find_skill(text):

    text = text.lower()


    for keyword, plugin in loaded_skills.items():

        if keyword in text:

            return plugin


    return None
