commands = {}

def register(name, func):
    commands[name] = func

def execute(command, args):
    if command in commands:
        commands[command](args)
    else:
        print(f"Unknown command: {command}")
        print("Type 'help' to see available commands.")

def get_commands():
    return commands
