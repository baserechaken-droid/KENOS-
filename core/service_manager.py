import threading

_services = {}


class Service:

    def __init__(self, name, target):

        self.name = name
        self.target = target
        self.thread = None
        self.running = False

    def start(self):

        if self.running:
            return False

        self.running = True

        self.thread = threading.Thread(
            target=self.target,
            daemon=True,
            name=self.name
        )

        self.thread.start()

        return True

    def stop(self):

        self.running = False

    def status(self):

        return self.running


def register(name, target):

    if name in _services:
        return False

    _services[name] = Service(name, target)

    return True


def unregister(name):

    if name not in _services:
        return False

    _services.pop(name)

    return True


def start(name):

    if name not in _services:
        return False

    return _services[name].start()


def stop(name):

    if name not in _services:
        return False

    _services[name].stop()

    return True


def restart(name):

    if name not in _services:
        return False

    stop(name)

    start(name)

    return True


def running(name):

    if name not in _services:
        return False

    return _services[name].status()


def get(name):

    return _services.get(name)


def list_services():

    return _services


def count():

    return len(_services)
