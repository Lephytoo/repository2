import json

# Mock data for menu and bestselling books
menu_items = {
    'food': ['Sandwich', 'Cake'],
    'drinks': ['Coffee', 'Tea'],
    'specials': ['Special Salad']
}
bestselling_books = ['The Great Gatsby', '1984']

# Customer class definition
class Customer:
    def __init__(self, name, address, order):
        self.name = name
        self.address = address
        self.order = order

    def to_dict(self):
        """Convert customer object to dictionary for JSON serialization."""
        return {
            'name': self.name,
            'address': self.address,
            'order': self.order
        }

def display_menu():
    """Display the menu items."""
    print("\nMenu:")
    print("Food: " + ", ".join(menu_items['food']))
    print("Drinks: " + ", ".join(menu_items['drinks']))
    print("Specials: " + ", ".join(menu_items['specials']))

def display_books():
    """Display the bestselling books."""
    print("\nBestselling Books: " + ", ".join(bestselling_books))

def customer_order():
    """Handles taking the customer order and saving/loading it to/from a file."""
    display_menu()
    display_books()

    order = []
    while True:
        item = input("\nEnter an item from the menu or book (or type 'done' to finish): ").strip()
        if item.lower() == 'done':
            break
        # Check if the item exists in the menu or book list
        if item in menu_items['food'] or item in menu_items['drinks'] or item in bestselling_books or item in menu_items['specials']:
            order.append(item)
        else:
            print("Item not found. Please choose again.")

    if order:
        name = input("Enter your name: ").strip()
        address = input("Enter your address for delivery (if ordering books): ").strip()
        customer = Customer(name, address, order)

        # Serialize and save customer data to a file
        customer_data = customer.to_dict()
        filename = "customer_data.json"  # Save the data to a JSON file

        try:
            with open(filename, "w") as file:
                json.dump(customer_data, file, indent=4)
            print(f"\nThank you for your order, {name}!")
            print("Data successfully written to:", filename)

            # Load the customer data from the file to verify
            with open(filename, "r") as file:
                loaded_data = json.load(file)
                print("\nData loaded from:", filename)
                print(loaded_data)
        except IOError:
            print(f"An error occurred while handling the file: ")
    else:
        print("No items ordered.")

def update_books():
    
    while True:
        print("\nCurrent Bestselling Books:")
        print(", ".join(bestselling_books))
        
        action = input("\nWould you like to 'add', 'remove', or 'update' books? (type 'done' to finish): ").strip().lower()
        
        if action == 'done':
            break
        
        if action == 'add':
            new_book = input("Enter the title of the book to add: ").strip()
            if new_book and new_book not in bestselling_books:
                bestselling_books.append(new_book)
                print(f"'{new_book}' has been added to the bestselling books.")
            else:
                print("Invalid input or book already exists.")
                
        elif action == 'remove':
            book_to_remove = input("Enter the title of the book to remove: ").strip()
            if book_to_remove in bestselling_books:
                bestselling_books.remove(book_to_remove)
                print(f"'{book_to_remove}' has been removed from the bestselling books.")
            else:
                print("Book not found in the list.")
                
        elif action == 'update':
            old_title = input("Enter the current title of the book to update: ").strip()
            if old_title in bestselling_books:
                new_title = input("Enter the new title: ").strip()
                index = bestselling_books.index(old_title)
                bestselling_books[index] = new_title
                print(f"'{old_title}' has been updated to '{new_title}'.")
            else:
                print("Book not found in the list.")
                
        else:
            print("Invalid action. Please choose 'add', 'remove', or 'update'.")
            
    filename = "bestselling_books.json"
    try:
        with open(filename, "w") as file:
            json.dump(bestselling_books, file, indent=4)
        print(f"\nUpdated bestselling books saved to {filename}.")
    except IOError:
        print("An error occurred while saving the updated book list.")


def view_customers():
    """View customer details."""
    filename = "customer_data.json"
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            print("\nCustomer Details:")
            print(json.dumps(data, indent=4))
    except IOError:
        print(f"An error occurred while reading the file.")

def update_menu():
    while True:
        print("\nWhat would you like to update?")
        print("1. Add a new food item")
        print("2. Add a new drink item")
        print("3. Add a new special")
        print("4. Exit")
        choice = input("Enter your choice: ")
 
        if choice == '1':
            new_item = input("Enter the new food item: ").strip()
            menu_items['food'].append(new_item)
            print(f"{new_item} added to the food menu.")
        elif choice == '2':
            new_item = input("Enter the new drink item: ").strip()
            menu_items['drinks'].append(new_item)
            print(f"{new_item} added to the drinks menu.")
        elif choice == '3':
            new_special = input("Enter the new special item: ").strip()
            menu_items['specials'].append(new_special)
            print(f"{new_special} added to today's specials.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")



update_books()
# update_menu()
customer_order()
