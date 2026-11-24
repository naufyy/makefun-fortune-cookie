"""Write one line of fortune-cookie wisdom for developers to /output/entry.txt.

The line is about a familiar trap: a legacy function that nobody owns. Fix just
one line in it and `git blame` now shows your name on that line. From then on
you are the person people ask about the whole function. "Blame" here means both
the tool and the responsibility that comes with it.
"""
from pathlib import Path

LINE = "Fix one line in the legacy function nobody owns, and git blame will gladly make it yours."
OUTPUT = Path("/output/entry.txt")


def main() -> None:
    assert 1 <= len(LINE) <= 120 and "\n" not in LINE and LINE.strip()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
