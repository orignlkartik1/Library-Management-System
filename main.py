"""
Library Management System - Main Entry Point
Demonstrates OOP concepts: Encapsulation, Inheritance, Polymorphism, and Composition
"""

from models import Book, User, Library, Transaction
from models.user import UserType
from models.transaction import TransactionType


def main():
    """
    Main function to demonstrate the Library Management System.
    """
    print("=" * 60)
    print("Library Management System - Demo")
    print("=" * 60)
    
    # Create a library
    library = Library("Central Library", "New Delhi")
    print(f"\nCreated: {library}")
    
    # Add books to the library
    print("\n--- Adding Books ---")
    books_data = [
        ("ISBN001", "Python Programming", "Guido van Rossum", "Programming", 2020, 3),
        ("ISBN002", "Data Structures", "Mark Allen Weiss", "Programming", 2018, 2),
        ("ISBN003", "Design Patterns", "Gang of Four", "Software Design", 2019, 2),
        ("ISBN004", "Clean Code", "Robert C. Martin", "Programming", 2017, 4),
        ("ISBN005", "The Hobbit", "J.R.R. Tolkien", "Fantasy", 2012, 5),
    ]
    
    for isbn, title, author, genre, year, qty in books_data:
        success = library.add_book(isbn, title, author, genre, year, qty)
        if success:
            print(f"  ✓ Added: {title}")
    
    # Add users to the library
    print("\n--- Registering Users ---")
    users_data = [
        ("U001", "Kartik Singh", "kartik@email.com", "9876543210", UserType.STUDENT),
        ("U002", "Priya Sharma", "priya@email.com", "9876543211", UserType.STUDENT),
        ("U003", "Prof. Rajesh", "rajesh@email.com", "9876543212", UserType.FACULTY),
        ("U004", "Amit Kumar", "amit@email.com", "9876543213", UserType.STAFF),
    ]
    
    for user_id, name, email, phone, user_type in users_data:
        success = library.add_user(user_id, name, email, phone, user_type)
        if success:
            print(f"  ✓ Registered: {name} ({user_type.value})")
    
    # Demonstrate borrowing books
    print("\n--- Borrowing Books ---")
    borrow_operations = [
        ("U001", "ISBN001"),
        ("U001", "ISBN002"),
        ("U002", "ISBN004"),
        ("U003", "ISBN003"),
        ("U003", "ISBN005"),
    ]
    
    for user_id, isbn in borrow_operations:
        success, message = library.borrow_book(user_id, isbn)
        status = "✓" if success else "✗"
        print(f"  {status} {message}")
    
    # Display user details
    print("\n--- User Details ---")
    for user_id in ["U001", "U002", "U003"]:
        user = library.get_user(user_id)
        if user:
            print(f"\n  User: {user.name}")
            print(f"  Email: {user.email}")
            print(f"  Type: {user.user_type.value}")
            print(f"  Books Borrowed: {user.borrowed_count}/{user.get_borrowing_limit()}")
            for isbn in user.borrowed_books:
                book = library.get_book(isbn)
                if book:
                    print(f"    - {book.title}")
    
    # Display available books
    print("\n--- Available Books ---")
    available = library.get_available_books()
    for book in available:
        print(f"  • {book.title} ({book.available_quantity} available)")
    
    # Search functionality
    print("\n--- Search by Author (Guido) ---")
    results = library.search_books_by_author("Guido")
    for book in results:
        print(f"  • {book}")
    
    # Demonstrate return
    print("\n--- Returning Books ---")
    return_operations = [
        ("U001", "ISBN001"),
        ("U002", "ISBN004"),
    ]
    
    for user_id, isbn in return_operations:
        success, message, fine = library.return_book(user_id, isbn)
        status = "✓" if success else "✗"
        print(f"  {status} {message}")
    
    # Display library statistics
    print("\n--- Library Statistics ---")
    stats = library.get_library_statistics()
    for key, value in stats.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
    
    # Display all transactions
    print("\n--- All Transactions ---")
    all_trans = Transaction.get_all_transactions()
    for trans in all_trans:
        details = trans.get_transaction_details()
        print(f"  {trans}")
    
    print("\n" + "=" * 60)
    print("Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()