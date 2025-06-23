from utils import validate_phone

def change_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        raise ValueError("Usage: change <name> <new_phone>")
    name, new_phone = args
    if name in contacts:
        if validate_phone(new_phone) is False:
            raise ValueError("Invalid phone number format. Use +380XXXXXXXXX.")
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Error: Contact not found."
