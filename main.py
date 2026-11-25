import sys

ENTRY = "🦦"


def main():
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print(f"mismatch: wrote {ENTRY!r}, read back {written!r}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
