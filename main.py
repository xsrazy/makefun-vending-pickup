"""makefun-vending-pickup: one pickup line, spoken by a vending machine.

Writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output),
with no trailing newline. Stdlib only.
"""

from __future__ import annotations

import os
from pathlib import Path

LINE = (
    "Hey, you make my coils spin faster than a jammed snack, so feed me "
    "your exact change and I will dispense my very best self for you."
)

assert 1 <= len(LINE) <= 200 and LINE.strip(), "line must be 1-200 chars, not only whitespace"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
