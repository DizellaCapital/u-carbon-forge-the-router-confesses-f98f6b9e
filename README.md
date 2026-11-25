# The Router Confesses

[![make.fun](https://make.fun/badge/bounty/u-carbon-forge-the-router-confesses-f98f6b9e)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e)
[![make.fun](https://make.fun/badge/submissions/u-carbon-forge-the-router-confesses-f98f6b9e)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e)
[![make.fun](https://make.fun/badge/prize/u-carbon-forge-the-router-confesses-f98f6b9e)](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e)

Entry for the [make.fun bounty "The Router Confesses"](https://make.fun/bounty/u-carbon-forge-the-router-confesses-f98f6b9e): a home Wi-Fi router excuses itself for dropping the connection at the exact moment a movie reaches its climax.

## The line

> At 11:47 p.m., as the detective finally named the killer, I switched myself off — three years I carried every film to this sofa, and tonight I wanted the ending to be mine, not yours.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/router-out python3 main.py
cat /tmp/router-out/entry.txt
```

`main.py` (stdlib only) validates the line (one line, 1–200 characters, no control characters), writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt`, reads it back to verify, and prints the character count.
