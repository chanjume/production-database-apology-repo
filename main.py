#!/usr/bin/env python3
"""Write one production-database apology line to /output/entry.txt.

One line, 1-200 characters. The apology turns on one concrete, real
detail -- DROP TABLE run on production instead of staging at 4:47 p.m. --
and the twist lands in the last words: the career sits in the same
Tuesday backup as the data, and that backup has never been tested.
Deadpan, specific, and believable enough to hurt. One line, 153 characters.
"""
import os

LINE = "Sorry — at 4:47 p.m. I ran DROP TABLE on production instead of staging. Your data is safe in Tuesday's backup; my career is in the same backup, untested."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars")


if __name__ == "__main__":
    main()
