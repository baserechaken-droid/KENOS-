from command_manager import list_plugins
from core.console import title

NAME = "plugins"
DESCRIPTION = "List loaded plugins"


def run(args):

    title("LOADED PLUGINS")

    plugins = list_plugins()

    for name in sorted(plugins):
        print(f"✓ {name}")

    print()
    print(f"Total: {len(plugins)} plugins")
    print()
