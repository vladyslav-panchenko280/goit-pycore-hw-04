from utils import validate_phone

def add_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        raise ValueError("Usage: add <name> <phone>")
    name, phone = args
    if validate_phone(phone) is False:
        raise ValueError("Invalid phone number format. Use +380XXXXXXXXX.")
    contacts[name] = phone
    return "Contact added."