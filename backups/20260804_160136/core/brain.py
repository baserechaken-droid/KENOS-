from core.nlp import parse
from command_manager import exists, get


def think(text):

    parsed = parse(text)

    if parsed is None:
        return False

    command, args = parsed

    if exists(command):
        get(command).run(args)
        return True

    return False
