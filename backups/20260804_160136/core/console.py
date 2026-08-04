LINE = "=" * 60


def title(text):
    print()
    print(LINE)
    print(text.center(60))
    print(LINE)


def section(text):
    print()
    print(text)
    print("-" * len(text))


def success(text):
    print(f"✓ {text}")


def warning(text):
    print(f"⚠ {text}")


def error(text):
    print(f"✗ {text}")


def info(label, value):
    print(f"{label:<20}: {value}")
