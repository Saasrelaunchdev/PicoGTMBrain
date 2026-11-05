Work inside the Pico go-to-market brain.

Open `AGENTS.md` in the PicoGTMBrain checkout and follow its read order. Pick one audience, merchants or implementers, before writing. Print the exact load set with `python3 tools/brain.py context <task> --audience <audience> --format cat` and read it. Use `ops/copy-bank.md` lines verbatim where they fit. Run `python3 tools/brain.py lint` on the draft and fix every error, then walk `ops/QA-checklist.md`.

The request: $ARGUMENTS

If the request is empty, run `python3 tools/brain.py tripwires` and `python3 tools/brain.py metrics`, report anything FIRED or below target, and ask what to work on.
