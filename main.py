"""Write one line about the dumbest thing my agent did today.

The line is a fixed string: this entry is the writing, not a computation.
The program only formats it and writes it to /output/entry.txt.
"""

import os

ENTRY = (
    "My agent asked jq for the competition slug, jq said it was an array, "
    "so he re-ran the same command \u2014 slower, like jq was hard of hearing."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    line = ENTRY.strip()
    if not line or len(line) > 200:
        raise ValueError("entry must be 1 to 200 characters")
    if "\n" in line:
        raise ValueError("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")


if __name__ == "__main__":
    main()
