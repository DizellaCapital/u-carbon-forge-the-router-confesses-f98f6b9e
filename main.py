"""The Router Confesses — entry program, variant 1.

One line a home Wi-Fi router says to excuse itself for dropping the
connection at the exact moment a movie reaches its climax. At 11:47
p.m., the second the detective names the killer, the router goes
dark — three years it has carried this house's films, and nobody has
ever once thanked the little blinking box. The scene is specific — a
time, a detective, a killer's name — and the twist is the router's
grudge: it is not sorry about the film, it is sorry nobody ever
thanked the appliance that carried it.

The program enforces the bounty limits — a single line of 1 to 200
characters — and writes the line to entry.txt, verifying the write
by reading it back.
"""

import os
import sys

LINE = "At 11:47 p.m., the second the detective named the killer, I went dark \u2014 three years I have carried this house's films, and nobody has ever once thanked the little blinking box."

MAX_CHARS = 200


def issues(line):
    """List every way the line breaks the bounty limits, if any."""
    bad = []
    if not line or line.strip() != line:
        bad.append("empty or padded")
    if len(line) > MAX_CHARS:
        bad.append("over 200 characters")
    if "\n" in line or "\r" in line:
        bad.append("more than one line")
    return bad


def main():
    bad = issues(LINE)
    if bad:
        print("invalid entry: " + "; ".join(bad), file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        if f.read() != LINE:
            print("read-back mismatch", file=sys.stderr)
            return 1
    print("wrote %d characters to %s" % (len(LINE), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
