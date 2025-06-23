from pathlib import Path

MAX_ARGS_COUNT = 2

def validate_args(args: list[str]) -> Path:
    if len(args) != MAX_ARGS_COUNT:
        raise ValueError("Usage: python main.py <path_to_directory>")
        sys.exit(1)
    path = Path(args[1])

    if not path.exists():
        raise ValueError("Error: path does not exist.")

    if not path.is_dir():
        raise ValueError("Error: path is not a directory.")
        sys.exit(1)

    return path