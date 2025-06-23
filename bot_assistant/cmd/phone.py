def show_contact(args: list, contacts: dict) -> str:
    if len(args) != 1:
        return "Usage: phone <name>"
    name = args[0]
    return contacts.get(name, "Error: Contact not found.")