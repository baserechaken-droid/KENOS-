#!/usr/bin/env python3

import os
import shutil

BACKUP_DIR = "backups"


def latest_backup():

    backups = sorted(os.listdir(BACKUP_DIR))

    if not backups:

        print("No backups found.")

        return None

    return os.path.join(BACKUP_DIR, backups[-1])


def main():

    backup = latest_backup()

    if backup is None:

        return

    print(f"Latest backup: {backup}")

    print("Restore functionality will be added in a future update.")


if __name__ == "__main__":

    main()
