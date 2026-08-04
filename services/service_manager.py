SERVICES = {}


def register(name, service):
    SERVICES[name] = service


def get(name):
    return SERVICES.get(name)


def exists(name):
    return name in SERVICES


def list_services():
    return SERVICES
