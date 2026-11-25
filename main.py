"""The Router Confesses — v3.

A home Wi-Fi router excuses itself for dropping the connection at the
exact moment a movie reaches its climax. One line, 1-200 characters.
"""

import os

LINE = (
    "At 11:47 p.m., the detective said the name, and I fainted \u2014 "
    "three years of carrying your films, and not one of you ever "
    "asked how my evening was going."
)


def main():
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"line is {len(LINE)} chars, must be 1-200")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single line")
    if any(ord(ch) < 32 for ch in LINE):
        raise SystemExit("line must not contain control characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == LINE, "round-trip mismatch"
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()
