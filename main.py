"""Write the honest appliance error message to the output file.

The grader runs this program with an empty writable output directory
and reads the single text it writes. The text must stand alone as one
honest error message an appliance could show: it names a plausible
fault, in the appliance's own flat, put-upon voice, with the laugh
coming out of the truth of the fault and landing in the last word.
"""

import os
from pathlib import Path

ENTRY = "Error: drain blocked by one sock. I am now an expensive bucket."


def output_path() -> Path:
    """Return the entry file, honouring the grader's output directory."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(directory) / "entry.txt"


def main() -> None:
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
