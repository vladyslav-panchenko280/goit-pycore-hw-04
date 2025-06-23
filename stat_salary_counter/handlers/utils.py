DATA_PROPS_LENGTH = 2
DATA_SPLIT_CHARACTER = ","

def validate_raw_data_structure(parts: list[str, str]) -> None:
    if len(parts) != DATA_PROPS_LENGTH:
        raise ValueError(f"Invalid structure in {parts}. Each row should only consist from name (str) and salary (number)")

def validate_raw_data_name(name: str, parts: list[str, str]) -> int:
    if not name.strip():
        raise ValueError(f"Invalid name in {parts}")
    
def validate_raw_data_salary(salary: str, parts: list[str, str]) -> int:
    try:
        salary_int = int(salary)
    except ValueError:
        raise ValueError(f"Invalid salary in {parts}")
    
    return salary_int