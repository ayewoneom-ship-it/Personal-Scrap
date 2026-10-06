# happy one month 💛🖤

Two little Python gifts for my boyfriend, both made for our one-month anniversary (Sept 6 → Oct 6).

## 1. `for_you.py`: a gift you send as code

A terminal program that draws a beating heart out of the words *ILOVETALKINGTOYOU*,
counts how many days we've been together, and types out a little message.

Send him the file and tell him to run:

```bash
python3 for_you.py
```

Change `NAME`, `FROM`, and `WORDS` at the top first.

## 2. `love_site/`: a website made with Python

`love_site/build.py` takes your settings (names, dates, our story, reasons I like you)
and builds a website into `docs/index.html`. The website has:

- a "happy one month" header with floating hearts (tap the big heart 💛)
- a live counter showing how long we've been together, down to the second
- our story as a timeline, from just friends in high school to now
- a heart going back and forth between Michigan and Purdue, plus the distance in miles (worked out in Python)
- an optional countdown to your next visit
- cards that flip over to show things I like about you
- a "will you be my boyfriend for another month?" question where the **No** button runs away 😤

### Make it yours

1. Open `love_site/build.py` and edit the **EDIT ME** section: his name, your name, your city's
   coordinates, the next visit date, the timeline, and the reasons.
2. Build it and preview it:
   ```bash
   python3 love_site/build.py --serve
   ```
   You don't need to install anything. It only uses Python's standard library.

### Send him a link (free)

1. Commit and push the updated `docs/index.html`.
2. On GitHub, go to **Settings → Pages**. Under "Build and deployment" choose
   **Deploy from a branch**, pick your branch, select the **/docs** folder, then click **Save**.
3. A minute later it's live at `https://<your-username>.github.io/<repo-name>/`. Text him that link 💌

(Your repo may need to be public for Pages to work on a free account.)
