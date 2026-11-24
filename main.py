"""Write the houseplant out-of-office entry to /output/entry.txt.

One line, a monstera climbing the bookshelf for sunlight; the email
only gets read once it reaches the top. 104 characters, no newline.
"""

from pathlib import Path

ENTRY = "Out of office: I'm halfway up the bookshelf chasing sunlight. Your email gets read when I reach the top."


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
