import re

def validate_phone(phone: str) -> bool:
    return bool(re.fullmatch(r"\+380\d{9}", phone))