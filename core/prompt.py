from datetime import datetime


def get_prompt():

    now = datetime.now().strftime("%H:%M:%S")

    return (
        "\n"
        "╭─ 🤖 KenOS AI | 🟢 ONLINE | 🕒 "
        + now +
        " ─╮\n"
        "╰─➤ "
    )
