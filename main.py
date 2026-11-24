"""Last Text at One Percent — one-line entry for make.fun.

Writes the phone's final 1%-battery text to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3 standard library only.
"""

import os

LINE = "Final text: 1% left. I have hidden your passwords, eaten your storage, and I regret nothing. Except the cracked screen. That one hurt."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
