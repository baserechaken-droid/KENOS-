#!/usr/bin/env python3

import shutil
from datetime import datetime

name = datetime.now().strftime("kenos_%Y%m%d_%H%M%S")

destination = f"backups/{name}"

shutil.copytree(".", destination,
                ignore=shutil.ignore_patterns(
                    "__pycache__",
                    "backups"
                ))

print("Backup created:")
print(destination)
