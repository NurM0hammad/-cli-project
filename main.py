#!/usr/bin/env python3
from contacts import ContactBook
from storage import load_contacts, save_contacts
from validation import validate_name, validate_phone, validate_email


class ContactBookCLI:
    def __init__(self):
        self.contact_book = ContactBook(load_contacts())

    def display_menu(self):
        print("\n=========== MENU ===========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Exit")
        print("============================")

    def run(self):
        print("Welcome to the Contact Book CLI System!")

        while True:
            self.display_menu()
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.remove_contact()
            elif choice == '5':
                self.exit_program()
                break
            else:
                print("Invalid choice. Please enter a number between 1-5.")

    def add_contact(self):
        print("\n=== Add New Contact ===")
        try:
            name = input("Enter Name: ").strip()
            if not validate_name(name):
                raise ValueError("Name must contain only letters and spaces")

            phone = input("Enter Phone Number: ").strip()
            if not validate_phone(phone):
                raise ValueError(
                    "Phone number must contain only digits (10-15 digits)")

            email = input("Enter Email: ").strip()
            if not validate_email(email):
                raise ValueError("Invalid email format")

            address = input("Enter Address: ").strip()
            if not address:
                raise ValueError("Address cannot be empty")

            self.contact_book.add_contact(name, email, phone, address)
            save_contacts(self.contact_book.contacts)
            print("\nContact added successfully!")
        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

    def view_contacts(self):
        contacts = self.contact_book.list_contacts()
        if not contacts:
            print("\nNo contacts found.")
            return

        print("\n===== All Contacts =====")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name : {contact['name']}")
            print(f"   Phone : {contact['phone']}")
            print(f"   Email : {contact['email']}")
            print(f"   Address: {contact['address']}")
        print("========================")

    def search_contact(self):
        search_term = input("\nEnter search term (name/email/phone): ").strip()
        if not search_term:
            print("Search term cannot be empty")
            return

        results = self.contact_book.search_contacts(search_term)
        if not results:
            print("\nNo matching contacts found.")
            return

        print("\nSearch Result:")
        for contact in results:
            print(f"\nName : {contact['name']}")
            print(f"Phone : {contact['phone']}")
            print(f"Email : {contact['email']}")
            print(f"Address: {contact['address']}")

    def remove_contact(self):
        phone = input(
            "\nEnter the phone number of the contact to delete: ").strip()
        if not phone:
            print("Phone number cannot be empty")
            return

        confirm = input(
            f"Are you sure you want to delete contact with phone {phone}? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Deletion cancelled.")
            return

        if self.contact_book.delete_contact_by_phone(phone):
            save_contacts(self.contact_book.contacts)
            print("\nContact deleted successfully!")
        else:
            print("\nContact not found.")

    def exit_program(self):
        save_contacts(self.contact_book.contacts)
        print("\nThank you for using the Contact Book CLI System. Goodbye!")


if __name__ == '__main__':
    ContactBookCLI().run()
