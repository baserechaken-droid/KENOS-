import platform

NAME = "neofetch"
DESCRIPTION = "Display KenOS information"


def run(args):

    print(r"""

██╗  ██╗███████╗███╗   ██╗ ██████╗ ███████╗
██║ ██╔╝██╔════╝████╗  ██║██╔═══██╗██╔════╝
█████╔╝ █████╗  ██╔██╗ ██║██║   ██║███████╗
██╔═██╗ ██╔══╝  ██║╚██╗██║██║   ██║╚════██║
██║  ██╗███████╗██║ ╚████║╚██████╔╝███████║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝

""")

    print("OS        :", "KenOS AI Edition")
    print("Python    :", platform.python_version())
    print("Machine   :", platform.machine())
    print("Processor :", platform.processor())
    print()
