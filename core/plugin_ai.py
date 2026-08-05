from plugin_loader import get_plugins


def tokenize(text):

    return {
        word.strip(".,!?").lower()
        for word in text.split()
        if word.strip()
    }


def score(plugin, text):

    text_words = tokenize(text)

    module = get_plugins().get(plugin)

    if not module:

        return 0

    score = 0

    #
    # Plugin name
    #

    if plugin.lower() in text.lower():

        score += 10

    #
    # Skills
    #

    skills = getattr(
        module,
        "SKILLS",
        []
    )

    for skill in skills:

        words = tokenize(skill)

        if words <= text_words:

            score += 8

        elif words & text_words:

            score += 3

    #
    # Description
    #

    desc = getattr(
        module,
        "DESCRIPTION",
        ""
    ).lower()

    for word in text_words:

        if word in desc:

            score += 1

    return score


def best_plugin(text):

    best = None

    best_score = 0

    for plugin in get_plugins():

        s = score(plugin, text)

        if s > best_score:

            best_score = s

            best = plugin

    if best_score >= 5:

        return best

    return None

