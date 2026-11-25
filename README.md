# One Emoji, One Smile

[![make.fun](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![Rank](https://make.fun/u-0xkianno-one-emoji-one-smile-5470751f/xiangbingxi/makefun-one-emoji-one-smile/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)
[![Reward](https://make.fun/u-0xkianno-one-emoji-one-smile-5470751f/xiangbingxi/makefun-one-emoji-one-smile/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f)

Entry for the make.fun bounty [One Emoji, One Smile](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f).

## What it does

`main.py` writes exactly one emoji to `/output/entry.txt`:

🦦

Nothing else — no words, no caption, no explanation. UTF-8, no trailing newline.

## Run

```sh
python3 main.py
```

After running, `/output/entry.txt` holds a single character (4 bytes in UTF-8), and the program reads it back to check it matches exactly, exiting with an error if it does not.
