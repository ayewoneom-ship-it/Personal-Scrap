"""
build.py - turns the stuff below into a cute little website for him 💛🖤

How to use:
    1. Edit the settings in the "EDIT ME" section below.
    2. Run:   python build.py            -> writes ../docs/index.html
              python build.py --serve    -> also opens it in your browser
    3. Send him the link (see README.md for free hosting with GitHub Pages).

No pip installs needed - only Python's standard library.
"""

import argparse
import html
import json
import math
import webbrowser
from datetime import date, datetime
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

# ───────────────────────────── EDIT ME ─────────────────────────────

HIS_NAME = "Vin"          # his name, e.g. "Jake"  (shows up all over the site)
MY_NAME = "Abby"            # your name, signs the bottom of the page

TOGETHER_SINCE = datetime(2026, 9, 6, 23, 59)   # Sept 6, 11:59pm  (year, month, day, hour, minute)

# where each of you is - used to calculate how many miles apart you are.
# Look up your city's latitude/longitude on Google Maps (right-click -> the numbers).
MY_PLACE = {"label": "Michigan", "lat": 42.2808, "lon": -83.7430}   # default: Ann Arbor
HIS_PLACE = {"label": "Purdue", "lat": 39.7737, "lon": -86.1751}    # Indianapolis, IN

# next time you'll see each other (YYYY, M, D) - or set to None to hide the countdown
NEXT_VISIT = datetime(2026, 10, 9, 19, 0)   # Friday Oct 9, 7pm  (year, month, day, hour, minute)

# our story, in order. (when, what)
TIMELINE = [
    ("This summer", "We went from fwb to friends to talking stage LOL. For like a whole month."),
    ("Sept 6", "You came up to Michigan and we made it official 💛"),
    ("Oct 6", "One whole month of us. Long distance and you're still my favorite person."),
    ("Next", "Many more drives between Michigan and Indianapolis, many more FaceTimes that go way too late."),
]

# tap-to-flip cards. Front = a little teaser, back = the real thing. Make these yours!
REASONS = [
    ("🌙", "Late nights", "You stay up on FaceTime with me even when you have an 8:30."),
    ("☺️", "You're caring", "You're the sweetest boyfriend and I love talking to you"),
    ("🤭", "My corner", "You're at my corner and I'm at yours and always will be"),
    ("🚗", "You showed up", "You drove all the way up to Michigan and gave me the best day."),
    ("💋", "Good Kisser", "I'm still impressed by our first kiss when you nearly fell LOL"),
    ("🫶", "Just you", "I like all of you hehe"),
]

# the big question at the end
QUESTION = "Will you be my boyfriend for another month? (and the one after that...)"
YES_MESSAGE = "YAY!! Happy one month, I really really like you 💛🖤"

# ──────────────────────── (no need to edit below) ────────────────────────

HERE = Path(__file__).resolve().parent
OUT_DIR = HERE.parent / "docs"   # GitHub Pages can serve straight from /docs


def miles_between(a, b):
    """Great-circle distance between two lat/lon points, in miles (haversine formula)."""
    earth_radius_mi = 3958.8
    lat1, lat2 = math.radians(a["lat"]), math.radians(b["lat"])
    dlat = lat2 - lat1
    dlon = math.radians(b["lon"] - a["lon"])
    h = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 2 * earth_radius_mi * math.asin(math.sqrt(h))


def render_timeline():
    items = []
    for when, what in TIMELINE:
        items.append(
            f'<li class="moment"><span class="when">{html.escape(when)}</span>'
            f'<p>{html.escape(what)}</p></li>'
        )
    return "\n".join(items)


def render_reasons():
    cards = []
    for emoji, front, back in REASONS:
        cards.append(
            '<button class="card" type="button" aria-label="flip card">'
            '<span class="card-inner">'
            f'<span class="face front"><span class="emoji">{emoji}</span>{html.escape(front)}</span>'
            f'<span class="face back">{html.escape(back)}</span>'
            '</span></button>'
        )
    return "\n".join(cards)


def build():
    miles = miles_between(MY_PLACE, HIS_PLACE)
    days = (datetime.now() - TOGETHER_SINCE).days
    display_name = HIS_NAME if HIS_NAME != "you" else "my favorite boilermaker"

    replacements = {
        "{{HIS_NAME}}": html.escape(display_name),
        "{{MY_NAME}}": html.escape(MY_NAME),
        "{{MY_PLACE}}": html.escape(MY_PLACE["label"]),
        "{{HIS_PLACE}}": html.escape(HIS_PLACE["label"]),
        "{{MILES}}": f"{miles:,.0f}",
        "{{DAYS_AT_BUILD}}": str(days),
        "{{TIMELINE}}": render_timeline(),
        "{{REASONS}}": render_reasons(),
        "{{QUESTION}}": html.escape(QUESTION),
        # json.dumps gives us safe JS literals
        "{{SINCE_JSON}}": json.dumps(TOGETHER_SINCE.isoformat()),
        "{{YES_MESSAGE_JSON}}": json.dumps(YES_MESSAGE),
        "{{NEXT_VISIT_JSON}}": json.dumps(NEXT_VISIT.isoformat() if NEXT_VISIT else None),
    }

    page = (HERE / "template.html").read_text(encoding="utf-8")
    for key, value in replacements.items():
        page = page.replace(key, value)

    OUT_DIR.mkdir(exist_ok=True)
    out = OUT_DIR / "index.html"
    out.write_text(page, encoding="utf-8")

    print(f"💛 built {out}")
    print(f"   {days} days together, {miles:,.0f} miles apart, {len(REASONS)} reasons (and counting)")
    return out


def serve(port=8000):
    handler = partial(SimpleHTTPRequestHandler, directory=str(OUT_DIR))
    url = f"http://localhost:{port}/"
    print(f"🖤 serving at {url}  (ctrl+c to stop)")
    webbrowser.open(url)
    with ThreadingHTTPServer(("localhost", port), handler) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nbye 💛")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build the one-month website 💛")
    parser.add_argument("--serve", action="store_true", help="open it in your browser after building")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    build()
    if args.serve:
        serve(args.port)
