from pathlib import Path
from utils import *
from handlers import *

def total_salary(path: str) -> tuple[int, int]:
    source_path = Path(path)
    
    validate_source_path(source_path)

    text = source_path.read_text(encoding=ENCODING_UTF_8)

    raw_data = prepare_raw_data(text)

    total = get_salary_total(raw_data)
    
    average = get_salary_average(total, len(raw_data))

    return (total, average)


total, average = total_salary('./salary_file.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
