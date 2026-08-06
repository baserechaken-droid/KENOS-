from plugin_loader import get_plugins

NAME = "plugins"
DESCRIPTION = "Manage installed plugins"

SKILLS = [
    "plugins",
    "plugin",
    "extensions",
    "skills"
]


def run(args):

    plugins = get_plugins()

    if not args:

        print()

        print("📦 Installed Plugins")

        print("-" * 40)

        for name in sorted(plugins):

            module = plugins[name]

            desc = getattr(
                module,
                "DESCRIPTION",
                ""
            )

            print(f"{name:<20} {desc}")

        print()

        return f"{len(plugins)} plugins installed."

    cmd = args[0].lower()

    if cmd == "count":

        total = len(plugins)

        print(total)

        return f"You currently have {total} plugins."

    if cmd == "search":

        if len(args) < 2:

            print("Usage: plugins search <keyword>")

            return

        keyword = " ".join(args[1:]).lower()

        print()

        found = False

        for name, module in sorted(plugins.items()):

            text = (
                name + " " +
                getattr(module, "DESCRIPTION", "")
            ).lower()

            if keyword in text:

                found = True

                print(name)

        if not found:

            print("No matching plugins.")

        print()

        return

    print("Unknown option.")

