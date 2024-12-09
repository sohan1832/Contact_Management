import json

def add_contact():
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone_number = input("Enter phone number: ")
    address = input("Enter address: ")

   
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = []

   
    for contact in contacts:
        if contact["phone_number"] == phone_number:
            print("Phone number already exists.")
            return

    
    new_contact = {
        "name": name,
        "email": email,
        "phone_number": phone_number,
        "address": address
    }
    contacts.append(new_contact)

    
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)

    print("Contact added successfully!")

def view_contacts():
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        print("No contacts found.")
        return

    if not contacts:
        print("No contacts found.")
    else:
        print("\nContacts:")
        for contact in contacts:
            print(f"Name: {contact['name']}")
            print(f"Email: {contact['email']}")
            print(f"Phone Number: {contact['phone_number']}")
            print(f"Address: {contact['address']}")
            print("-" * 20)