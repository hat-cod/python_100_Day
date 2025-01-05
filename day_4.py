# Function to add a new contact
def add_contact(phone_book):
    name = input("Enter the contact's name: ")
    phone = input(f"Enter {name}'s phone number: ")
    phone_book[name] = phone
    print(f"{name} has been added to your phone book!")

# Function to view all contacts
def view_contacts(phone_book):
    if phone_book:
        print("\nYour Phone Book:")
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")
    else:
        print("Your phone book is empty.")

# Function to search for a contact by name
def search_contact(phone_book):
    name = input("Enter the name of the contact you want to search for: ")
    if name in phone_book:
        print(f"{name}'s phone number is: {phone_book[name]}")
    else:
        print(f"No contact found with the name {name}.")

# Main loop to interact with the user
phone_book = {}

while True:
    print("\n--- Phone Book ---")
    action = input("Do you want to 'add' a contact, 'view' all contacts, 'search' for a contact, or 'exit'? ").lower()

    if action == "add":
        add_contact(phone_book)
    elif action == "view":
        view_contacts(phone_book)
    elif action == "search":
        search_contact(phone_book)
    elif action == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please choose 'add', 'view', 'search', or 'exit'.")



# Explanation:
# 1.Functions:

# add_contact(phone_book): This function allows the user to add a new contact (name and phone number) to the phone_book dictionary.
# view_contacts(phone_book): This function prints all the contacts in the phone book.
# search_contact(phone_book): This function allows the user to search for a contact by name and shows their phone number if found.

# 2.Dictionaries:
# The phone_book dictionary stores each contact's name as the key and their phone number as the value.

# 3.Loops:
# The program runs in a while loop to continuously interact with the user, allowing them to add, view, search, or exit.
# Error 

# 4.Handling:
# The program checks if the user enters a valid action (add, view, search, or exit). If the input is invalid, the program will prompt the user to choose a valid option.