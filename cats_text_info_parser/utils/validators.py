from pathlib import Path

ENCODING_UTF_8 = "utf-8"
TARGET_FILE_SUFFIX = ".txt"


def validate_source_path(pathObject: Path) -> None:
    if not pathObject.exists():
        raise FileExistsError(f"{pathObject} does not exist")

    if not pathObject.is_file() and pathObject.suffix != TARGET_FILE_SUFFIX:
        raise FileExistsError(f"{pathObject} is not valid {TARGET_FILE_SUFFIX} file")
    