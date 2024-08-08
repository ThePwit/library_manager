import datetime

# Dictionary to store book information
library = {}

# List to keep track of borrowed books
borrowed_books = []

# Function to add or update a book in the library
def add_book(book_id, title, author, quantity):
    if book_id in library:
        library[book_id]['quantity'] += quantity
        print("Quantity of {} in the library has been updated.".format(title))
    else:
        library[book_id] = {'title': title, 'author': author, 'quantity': quantity}
        print("{} has been added to the library.".format(title))

# Function to remove a book from the library
def remove_book(book_id):
    if book_id in library:
        print("{} has been removed from the library.".format(library[book_id]['title']))
        del library[book_id]
    else:
        print("Book with ID {} not found in the library.".format(book_id))

# Function to search for books by title or author
def search_book(keyword):
    matching_books = [book_id for book_id, book in library.items() if keyword in book['title'] or keyword in book['author']]
    return matching_books

# Function to display the entire library inventory sorted by book ID
def display_inventory():
    for book_id in sorted(library.keys()):
        print("Book ID: {}, Title: {}, Author: {}, Quantity: {}".format(book_id, library[book_id]['title'], library[book_id]['author'], library[book_id]['quantity']))

# Function to borrow a book and update inventory
def borrow_book(book_id, borrower_name, borrow_date):
    if book_id in library:
        if library[book_id]['quantity'] > 0:
            borrowed_books.append({'book_id': book_id, 'borrower_name': borrower_name, 'borrow_date': borrow_date})
            print("{} has been checked out by {} on {}.".format(library[book_id]['title'], borrower_name, borrow_date))
            library[book_id]['quantity'] -= 1
        else:
            print("Book with ID {} is out of stock.".format(book_id))
    else:
        print("Book with ID {} not found in the library.".format(book_id))

# Function to return a borrowed book and update inventory
def return_book(book_id):
    date = datetime.datetime.today()
    for book in borrowed_books:
        if book['book_id'] == book_id:
            print("{} has been returned by {} on {}.".format(library[book_id]['title'], book['borrower_name'], date.strftime('%m/%d/%Y')))
            borrowed_books.remove(book)
            library[book_id]['quantity'] += 1
            break

# Error handling for various scenarios
try:
    add_book(1, 'Python Programming', 'Guido van Rossum', 5)
    add_book(2, 'Data Science Handbook', 'Jake VanderPlas', 3)
    remove_book(3)  # Trying to remove a non-existent book
    borrow_book(1, 'Alice', '2022-01-15')
    borrow_book(3, 'Bob', '2022-01-20')  # Borrowing a book that is out of stock
    add_book(1, 'Python Deep Learning', 'Ivan Vasilev', 2)  # Adding a book with an existing ID
except Exception as e:
    print("An error occurred:", e)

# Simple menu-driven interface for user interaction
while True:
    print("\nLibrary Management System Menu:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display library inventory")
    print("5. Borrow a book")
    print("6. Return a book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        quantity = int(input("Enter Quantity: "))
        add_book(book_id, title, author, quantity)
    elif choice == '2':
        book_id = int(input("Enter Book ID to remove: "))
        remove_book(book_id)
    elif choice == '3':
        keyword = input("Enter search keyword: ")
        matching_books = search_book(keyword)
        print("Matching Book IDs:", matching_books)
    elif choice == '4':
        display_inventory()
    elif choice == '5':
        book_id = int(input("Enter Book ID to borrow: "))
        borrower_name = input("Enter Borrower Name: ")
        borrow_date = input("Enter Borrow Date: ")
        borrow_book(book_id, borrower_name, borrow_date)
    elif choice == '6':
        book_id = int(input("Enter Book ID to return: "))
        return_book(book_id)
    elif choice == '7':
        print("Exiting Library Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
