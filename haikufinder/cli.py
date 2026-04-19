from __future__ import annotations

import sys
from pathlib import Path

from haikufinder import HaikuFinder


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if argv:
        text = Path(argv[0]).read_text(encoding="utf-8")
    else:
        text = sys.stdin.read()
    for haiku in HaikuFinder(text).find_haikus():
        print(haiku[0])
        print("    %s" % haiku[1])
        print(haiku[2])
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
