# Handoff — One Emoji, One Smile

- Competition: https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f
- Entry text (user's wording, verbatim, one emoji): 🦦
- Character count: 1
- Byte count (UTF-8): 4 (`f0 9f a6 a6`)
- sha256 of `/output/entry.txt`: `85c80938ce3318ff9605bfab051f0588df4a002ab91c4d7c2fd5d6f911efa459`

## How it works

`main.py` writes the single otter emoji to `/output/entry.txt` with
`encoding="utf-8"` and `newline=""` (no trailing newline, no escapes,
no external files, no network). It then reads the file back and exits
with an error if what it reads differs by even one character from the
entry — that read-back check is the second-pass improvement over the
first version, which only wrote the file.

## Verification

- First version: ran clean, output 4 bytes / 1 character, sha256
  `85c80938ce3318ff9605bfab051f0588df4a002ab91c4d7c2fd5d6f911efa459`.
- Second version: ran twice, exit 0 both times; the two outputs are
  byte-identical (`cmp` clean) with the same sha256 as the first version.
- `entry.txt` bytes are identical to `prompt.txt` (exact match).
- Note: `/output/entry.txt` is shared with other workers on this
  machine and gets overwritten between runs by other entries, so
  verification captured each run's output to a uniquely named file
  immediately after the run. The program's own in-process read-back
  check passed on every run.
