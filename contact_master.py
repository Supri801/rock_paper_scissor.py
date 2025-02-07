import json
import os

CONTACTS_FILE = "contacts.json"

# Preload sample contacts if file doesn't exist
SAMPLE_CONTACTS = {
    "Susmitha": {"Phone": "9876543210", "Email": "surasurasusmitha@gmail.com"},
    "Vedhavathi": {"Phone": "8765432109", "Email": "Vedhavathi@gmail.com"},
    "Kavya": {"Phone": "7654321098", "Email": "VuddalaKavya@gmail.com"},
    "Juhi": {"Phone": "6543210987", "Email": "Shaikjuhi@gmail.com"},
    "Chandu": {"Phone": "5432109876", "Email": "Chandana@gmail.com"}
}

# Function to load contacts from the JSON file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    else:
        save_contacts(SAMPLE_CONTACTS)  # Save sample contacts if file doesn't exist
        return SAMPLE_CONTACTS

# Function to save contacts to the JSON file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts = load_contacts()
    
    if name in contacts:
        print("Contact already exists!")
        return
    
    contacts[name] = {"Phone": phone, "Email": email}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

# Function to view all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found!")
        return

    print("\n📝 Contact List:")
    print("-" * 40)
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {details['Phone']}")
        print(f"Email: {details['Email']}")
        print("-" * 40)

# Function to search for a contact
def search_contact():
    search_name = input("Enter the name to search: ").strip()
    contacts = load_contacts()

    if search_name in contacts:
        print("\n✅ Contact Found:")
        print("-" * 40)
        print(f"Name: {search_name}")
        print(f"Phone: {contacts[search_name]['Phone']}")
        print(f"Email: {contacts[search_name]['Email']}")
        print("-" * 40)
    else:
        print("❌ Contact not found!")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip()
    contacts = load_contacts()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"🗑️ Contact '{name}' deleted successfully!")
    else:
        print("❌ Contact not found!")

# Main menu
def main():
    while True:
        print("\n📞 ContactMaster - Contact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Exiting ContactMaster. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
