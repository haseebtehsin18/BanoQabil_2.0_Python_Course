# Abdul Haseeb Tehseen
# haseebtehsin97@gmail.com
# "IMPLEMENT EDIT CONTACT FEATURE"
# PROJECT NO.2

# Giving attributes for contact

class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

#initializing an empty list to store contacts
        
class AddressBook:
    def __init__(self):
        self.contacts = []

# creating a new contact and adding it to the list

    def add_contact(self, name, phone_number, email):
        contact = Contact(name, phone_number, email)
        self.contacts.append(contact)
        print("Contact added successfully.")

# printing details of each contact

    def display_contacts(self):
        print("Contacts:")
        for idx, contact in enumerate(self.contacts):
            print(f"{idx+1}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")

# checking if the index is valid then update the contact details

    def edit_contact(self, index, name, phone_number, email):
        if 0 <= index < len(self.contacts):
            contact = self.contacts[index]
            contact.name = name
            contact.phone_number = phone_number
            contact.email = email
            print("Contact edited successfully.")
        else:
            print("Invalid index.")

# adding sample contacts

def main():
    address_book = AddressBook()

    address_book.add_contact("haseeb", "1234567890", "haseeb@gmail.com")
    address_book.add_contact("hamza", "9876543210", "hamza@gmail.com")
    address_book.add_contact("basit", "123543765", "basit@gmail.com")
    address_book.add_contact("saad", "090912333", "saad@gmail.com")
    address_book.add_contact("shakeela", "030120213", "shakeela@gmail.com")

# display contacts

    address_book.display_contacts()

    index = int(input("Enter index of contact to edit: ")) - 1
    if 0 <= index < len(address_book.contacts):

# giving new details and editing contact
        
        name = input("Enter new name: ")
        phone_number = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address_book.edit_contact(index, name, phone_number, email)

# display updated contacts
        
        address_book.display_contacts()
    else:
        print("Invalid index.")

# calling the main function 
        
main()

