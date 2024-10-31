# contact_bot_manager.py

contacts = {}  # Словник для зберігання контактів

def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact '{name}' added."

def change_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact '{name}' updated."
    return f"Contact '{name}' not found."

def show_phone(name):
    if name in contacts:
        return f"{name}: {contacts[name]}"
    return f"Contact '{name}' not found."

def show_all():
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    return "No contacts available."
