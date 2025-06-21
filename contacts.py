class ContactBook:
    def __init__(self, contacts=None):
        self.contacts = contacts if contacts is not None else []

    def add_contact(self, name, email, phone, address):
        """Add a new contact with validation"""
        # Check for duplicate phone number
        if any(contact['phone'] == phone for contact in self.contacts):
            raise ValueError("Phone number already exists for another contact")

        new_contact = {
            'name': name,
            'email': email,
            'phone': phone,
            'address': address
        }
        self.contacts.append(new_contact)

    def list_contacts(self):
        """Return all contacts sorted by name"""
        return sorted(self.contacts, key=lambda x: x['name'].lower())

    def search_contacts(self, query):
        """Search contacts by name, email, or phone (partial matches)"""
        query = query.lower()
        results = []

        for contact in self.contacts:
            if (query in contact['name'].lower() or
                query in contact['email'].lower() or
                    query in contact['phone']):
                results.append(contact)

        return results

    def delete_contact_by_phone(self, phone):
        """Delete contact by phone number"""
        for i, contact in enumerate(self.contacts):
            if contact['phone'] == phone:
                self.contacts.pop(i)
                return True
        return False
