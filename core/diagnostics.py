import os
import platform


def startup_check():

    checks = [
        ("Python " + platform.python_version(), True),
        ("data/", os.path.exists("data")),
        ("logs/", os.path.exists("logs")),
        ("plugins/", os.path.exists("plugins")),
        ("core/", os.path.exists("core")),
        ("services/", os.path.exists("services")),
    ]


    for name, status in checks:

        if status:

            print(f"✓ {name}")

        else:

            print(f"✗ Missing {name}")


    print()
