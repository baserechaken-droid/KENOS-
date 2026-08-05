class Context:

    def __init__(self):

        self.last_plugin = None
        self.last_args = []
        self.last_command = ""
        self.last_result = ""


    def update(self, plugin, args, command="", result=""):

        self.last_plugin = plugin
        self.last_args = args
        self.last_command = command
        self.last_result = result


    def plugin(self):
        return self.last_plugin


    def args(self):
        return self.last_args


    def command(self):
        return self.last_command


    def result(self):
        return self.last_result


context = Context()
