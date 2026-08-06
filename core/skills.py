from plugin_loader import get_plugins


class SkillManager:

    def __init__(self):

        self.reload()


    def reload(self):

        self.skills = {}

        for name, module in get_plugins().items():

            self.skills[name] = {

                "name": name,

                "description": getattr(
                    module,
                    "DESCRIPTION",
                    ""),

                "skills": getattr(
                    module,
                    "SKILLS",
                    []),

                "module": module

            }


    def all(self):

        return self.skills


    def search(self, query):

        query = query.lower()

        matches = []

        for skill in self.skills.values():

            if query in skill["name"].lower():

                matches.append(skill)

                continue

            if query in skill["description"].lower():

                matches.append(skill)

                continue

            for keyword in skill["skills"]:

                if query in keyword.lower():

                    matches.append(skill)

                    break

        return matches


manager = SkillManager()

