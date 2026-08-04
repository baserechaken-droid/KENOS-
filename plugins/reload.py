from plugin_loader import reload_plugin, reload_all

NAME = "reload"
DESCRIPTION = "Reload plugins without restarting KenOS"


def run(args):

    if not args:

        print("Usage: reload <plugin|all>")

        return

    if args[0] == "all":

        reload_all()

        return

    reload_plugin(args[0])
