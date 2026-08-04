#!/usr/bin/env python3

import os
from datetime import datetime

VERSION = "8.0"


def banner():

    print()

    print("=" * 60)
    print("KENOS UPGRADE".center(60))
    print("=" * 60)

    print(f"Target Version : {VERSION}")
    print(f"Date           : {datetime.now()}")

    print()


def create(path):

    if os.path.exists(path):

        print(f"✓ {path}")

    else:

        os.makedirs(path, exist_ok=True)

        print(f"+ Created {path}")


def main():

    banner()

    create("logs")

    create("data")

    create("services")

    create("tools")

    print()

    print("Upgrade completed successfully.")

    print()


if __name__ == "__main__":

    main()
