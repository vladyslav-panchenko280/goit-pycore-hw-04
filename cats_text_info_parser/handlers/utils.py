DATA_PROPS_LENGTH = 3
DATA_SPLIT_CHARACTER = ","

def validate_raw_data_structure(parts: list[str, str]) -> None:
    if len(parts) != DATA_PROPS_LENGTH:
        raise ValueError(f"Invalid structure in {parts}. Each row should only consist from id (str), name (str) and age (number)")

def validate_raw_data_string(str_data: str, label: str, parts: list[str, str]) -> int:
    if not str_data.strip():
        raise ValueError(f"Invalid {label} in {parts}")
    
def validate_raw_data_age(age: str, parts: list[str, str]) -> int:
    try:
        age_int = int(age)
    except ValueError:
        raise ValueError(f"Invalid age in {parts}")
    
    return age_int