from .utils import DATA_SPLIT_CHARACTER, validate_raw_data_structure, validate_raw_data_age, validate_raw_data_string

def parse_to_list_of_dict(raw_data: list[str]) -> list[dict[str, str, int]]:
    cats_list: list[dict[str, str, int]] = []
    for record in raw_data:
        parts = record.split(DATA_SPLIT_CHARACTER)

        validate_raw_data_structure(parts)

        id, name, age = parts
        
        validate_raw_data_string(id, "id", parts)

        validate_raw_data_string(name, "name", parts)

        age_int = validate_raw_data_age(age, parts)
        
        cats_list.append({ "id": id, "name": name, "age": age_int })

    return cats_list