"""
for_you.py 💛🖤

Hi. Run me:   python3 for_you.py
(make your terminal window kinda big first)
"""

import math
import os
import sys
import time
from datetime import date

NAME = "Vin"                      # <- his name
FROM = "Abby"                       # <- your name
TOGETHER_SINCE = date(2026, 9, 6)
WORDS = "ILOVETALKINGTOYOU"       # the heart gets drawn out of these letters (no spaces)

GOLD = "\033[38;5;180m"
PINK = "\033[38;5;211m"
RED = "\033[38;5;204m"
DIM = "\033[2m"
BOLD = "\033[1m"
RESET = "\033[0m"
CLEAR = "\033[2J\033[H"
HIDE_CURSOR, SHOW_CURSOR = "\033[?25l", "\033[?25h"

if os.name == "nt":
    os.system("")  # turns on colors in the Windows terminal


def heart(scale):
    """Draw a heart using the curve (x² + y² - 1)³ - x²y³ ≤ 0, filled with WORDS."""
    rows = []
    i = 0
    for row in range(15, -15, -1):
        line = ""
        y = row / 10 / scale
        for col in range(-30, 30):
            x = col / 20 / scale
            if (x * x + y * y - 1) ** 3 - x * x * y ** 3 <= 0:
                line += WORDS[i % len(WORDS)]
                i += 1
            else:
                line += " "
        if line.strip():
            rows.append(line)
    return rows


def typewrite(text, color="", delay=0.045):
    for ch in text:
        sys.stdout.write(color + ch + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def main():
    width = 60
    sys.stdout.write(HIDE_CURSOR)
    try:
        # the heart beats a few times
        for beat in range(14):
            scale = 1.0 + 0.12 * abs(math.sin(beat * math.pi / 3.5))
            color = RED if beat % 2 else PINK
            sys.stdout.write(CLEAR)
            print("\n".join(color + BOLD + line.center(width) + RESET for line in heart(scale)))
            time.sleep(0.18)

        days = (date.today() - TOGETHER_SINCE).days
        print()
        typewrite(f"  hi {NAME} :)".center(width), GOLD)
        time.sleep(0.4)
        typewrite(f"  it's been {days} days since sept 6th.".center(width), PINK)
        if days >= 30:
            typewrite(f"  that's {days // 30} month{'s' if days >= 60 else ''} of us!!".center(width), PINK)
        time.sleep(0.4)
        typewrite("  friends since high school, and now this.".center(width))
        typewrite("  michigan -> purdue is far, but you never feel far.".center(width))
        time.sleep(0.6)
        typewrite(f"  happy one month 💛🖤   - {FROM}".center(width), GOLD + BOLD, delay=0.08)
        print(DIM + "\n  (yes i coded this for you. you're welcome)\n".center(width) + RESET)
    finally:
        sys.stdout.write(SHOW_CURSOR)


if __name__ == "__main__":
    main()
