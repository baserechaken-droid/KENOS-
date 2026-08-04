#!/usr/bin/env python3

import os
import shutil
from datetime import datetime

BACKUP_DIR = "backups"


def banner():

    print()

    print("=" * 60)
    print("KENOS UPDATE".center(60))
    print("=" * 60)
    print()


def backup():

    os.makedirs(BACKUP_DIR, exist_ok=True)

    name = datetime.now().strftime("%Y%m%d_%H%M%S")

    destination = os.path.join(BACKUP_DIR, name)

    shutil.copytree(
        ".",
        destination,
        ignore=shutil.ignore_patterns(
            "__pycache__",
            "backups",
            ".git"
        )
    )

    print(f"✓ Backup created: {destination}")


def verify():

    print()

    folders = (
        "core",
        "plugins",
        "services",
        "data",
        "logs",
        "tools"
    )

    for folder in folders:

        if os.path.isdir(folder):

            print(f"✓ {folder}")

        else:

            print(f"✗ Missing {folder}")

    print()


def main():

    banner()

    backup()

    verify()

    print("KenOS update completed.")
    print()


if __name__ == "__main__":

    main()
