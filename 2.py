import json


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    with open("contacts.json", "a") as f:
        f.write(json.dumps(contact) + "\n")
    print("Contact added successfully.")


def search_contact():
    name = input("Enter name to search: ")
    with open("contacts.json", "r") as f:
        for line in f:
            contact = json.loads(line)
            if contact["name"] == name:
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print(f"Address: {contact['address']}")
                return contact
        print("Contact not found.")
        return None


def edit_contact():
    contact = search_contact()
    if contact is not None:
        name = input("Enter new name (leave blank to keep current name): ")
        phone = input("Enter new phone number (leave blank to keep current phone number): ")
        email = input("Enter new email address (leave blank to keep current email address): ")
        address = input("Enter new address (leave blank to keep current address): ")
        if name:
            contact["name"] = name
        if phone:
            contact["phone"] = phone
        if email:
            contact["email"] = email
        if address:
            contact["address"] = address
        with open("contacts.json", "r") as f:
            lines = f.readlines()
        with open("contacts.json", "w") as f:
            for line in lines:
                old_contact = json.loads(line)
                if old_contact["name"] == contact["name"]:
                    f.write(json.dumps(contact) + "\n")
                else:
                    f.write(line)
        print("Contact updated successfully.")


def delete_contact():
    contact = search_contact()
    if contact is not None:
        with open("contacts.json", "r") as f:
            lines = f.readlines()
        with open("contacts.json", "w") as f:
            for line in lines:
                old_contact = json.loads(line)
                if old_contact["name"] != contact["name"]:
                    f.write(line)
        print("Contact deleted successfully.")


while True:
    print("1. Add contact")
    print("2. Search contact")
    print("3. Edit contact")
    print("4. Delete contact")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        edit_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Try again.")