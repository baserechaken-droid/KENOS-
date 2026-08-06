from plugin_loader import get_plugins
from core.aliases import find_alias


def tokenize(text):

    return {
        word.strip(".,!?").lower()
        for word in text.split()
        if word.strip()
    }


def score(plugin, text):

    words = tokenize(text)

    plugins = get_plugins()

    module = plugins.get(plugin)

    if module is None:

        return 0

    total = 0

    #
    # Plugin name
    #

    if plugin.lower() in text.lower():

        total += 20

    #
    # Skills
    #

    skills = getattr(
        module,
        "SKILLS",
        []
    )

    for skill in skills:

        skill_words = tokenize(skill)

        if skill_words <= words:

            total += 15

        elif skill_words & words:

            total += 5

    #
    # Description
    #

    description = getattr(
        module,
        "DESCRIPTION",
        ""
    ).lower()

    for word in words:

        if word in description:

            total += 1

    return total


def best_plugin(text):

    #
    # Alias lookup
    #

    alias = find_alias(text)

    if alias:

        return alias

    #
    # AI ranking
    #

    winner = None

    winner_score = -1

    for plugin in get_plugins():

        s = score(
            plugin,
            text
        )

        if s > winner_score:

            winner_score = s

            winner = plugin

    if winner_score < 5:

        return None

    return winner

