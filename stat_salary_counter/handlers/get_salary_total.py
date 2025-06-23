from .utils import DATA_SPLIT_CHARACTER, validate_raw_data_structure, validate_raw_data_salary, validate_raw_data_name

def get_salary_total(raw_data: list[str]) -> int:
    total = 0
    for record in raw_data:
        parts = record.split(DATA_SPLIT_CHARACTER)

        validate_raw_data_structure(parts)

        name, salary = parts
        
        validate_raw_data_name(name, parts)

        salary_int = validate_raw_data_salary(salary, parts)
        
        total += salary_int

    return total