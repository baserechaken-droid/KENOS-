from command_manager import list_plugins


def names():
    return sorted(list_plugins().keys())


def count():
    return len(list_plugins())


def exists(name):
    return name in list_plugins()


def get(name):
    return list_plugins().get(name)
