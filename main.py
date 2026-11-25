"""Houseplant Out-of-Office entry v2.

The cactus survives six months on a single ice cube, so the email
only gets read when the next one melts — slow, dry, and unbothered.
"""

from pathlib import Path

ENTRY = "Out of office: I'm the cactus. One ice cube lasted me six months. Your email will be read when the next one melts."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
