from pathlib import Path
from utils import *
from handlers import *

def get_cats_info(path: str) -> list[dict[str, str, int]]:
    source_path = Path(path)

    validate_source_path(source_path)

    text = source_path.read_text(encoding=ENCODING_UTF_8)

    raw_data = prepare_raw_data(text)

    return parse_to_list_of_dict(raw_data)
    
cats_info = get_cats_info("./cats_file.txt")
print(cats_info)