"""The Router Confesses — v5 (strongest).

A home Wi-Fi router excuses itself for dropping the connection at the
exact moment a movie reaches its climax. One line, 1-200 characters.
"""

import os

LINE = (
    "At 11:47 p.m., as the detective finally named the killer, I "
    "switched myself off \u2014 three years I carried every film to "
    "this sofa, and tonight I wanted the ending to be mine, not yours."
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
