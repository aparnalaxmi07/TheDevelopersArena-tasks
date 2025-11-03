# WEEK 3 PROJECT: CONTACT MANAGEMENT SYSTEM
# Developer's Arena Internship

contacts = {}

def add_contact(name, phone):
    """Adds a new contact."""
    contacts[name] = phone
    print(f"Contact '{name}' added successfully.")

def search_contact(name):
    """Search for a contact by name."""
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def display_contacts():
    """Display all contacts."""
    if contacts:
        print("\n----- Contact List -----")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
        print("------------------------")
    else:
        print("No contacts to display.")

# Main menu loop
while True:
    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Exit")

    choice = input("Enter your choice (1–4): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        add_contact(name, phone)

    elif choice == "2":
        name = input("Enter name to search: ")
        search_contact(name)

    elif choice == "3":
        display_contacts()

    elif choice == "4":
        print("Exiting Contact Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
