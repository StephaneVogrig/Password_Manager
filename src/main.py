import sys
from src.app import run_new, run_open

def main() -> int:
    argv = sys.argv
    argc = len(argv)

    if argc == 1:
        run_new()
        return 0

    if argc == 2:
        run_open(path=sys.argv[1])
        return 0

    print("Usage: password_manager [file]", file=sys.stderr)
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
