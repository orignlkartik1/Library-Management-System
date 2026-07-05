# Library Management System

A comprehensive Object-Oriented Python project demonstrating key OOP concepts through a library management system.

## Features

### Core Features
- **Book Management**: Add, search, and manage books in the library
- **User Management**: Register and manage library members with different user types
- **Transaction Tracking**: Track book borrowing and returning with automatic fine calculation
- **Search Functionality**: Search books by title, author, or genre
- **Library Statistics**: Get comprehensive statistics about library usage

## OOP Concepts Demonstrated

### 1. **Encapsulation**
- Private attributes using double underscore (`__`)
- Properties with getters and setters using `@property` decorator
- Example: `Book.__available_quantity` with validation in setter

### 2. **Composition**
- `Library` class uses composition to manage `Book`, `User`, and `Transaction` objects
- Objects work together to create a complete system

### 3. **Data Validation**
- Email validation in `User` class
- Quantity validation in `Book` class
- Input validation with meaningful error messages

### 4. **Enumerations**
- `UserType` enum for different user types (STUDENT, FACULTY, STAFF, VISITOR)
- `TransactionType` enum for transaction types (BORROW, RETURN)

### 5. **Class Variables and Methods**
- `total_books` in `Book` class to track total books created
- `total_users` in `User` class to track total users
- Class methods like `get_all_transactions()` in `Transaction` class

### 6. **Business Logic**
- Borrowing limits based on user type
- Automatic fine calculation for overdue books (Rs. 10 per day)
- Availability management for books

## Project Structure

```
Library-Management-System/
├── models/
│   ├── __init__.py          # Package initialization
│   ├── book.py              # Book class
│   ├── user.py              # User class and UserType enum
│   ├── transaction.py        # Transaction class and TransactionType enum
│   └── library.py           # Library class (main management system)
├── main.py                   # Demo application
└── README.md                 # This file
```

## Classes Overview

### Book Class
- **Attributes**: ISBN, title, author, genre, publication_year, quantity, available_quantity
- **Methods**: borrow(), return_book(), get_book_details()
- **Key Concepts**: Encapsulation, properties with validation

### User Class
- **Attributes**: user_id, name, email, phone, user_type, borrowed_books, is_active
- **Methods**: add_borrowed_book(), remove_borrowed_book(), can_borrow(), get_borrowing_limit()
- **Key Concepts**: Encapsulation, data validation, enum usage

### Transaction Class
- **Attributes**: user_id, book_isbn, transaction_type, transaction_date, due_date, return_date, fine
- **Methods**: is_overdue(), get_days_overdue(), process_return(), waive_fine()
- **Key Concepts**: Encapsulation, datetime handling, class methods

### Library Class
- **Methods**: 
  - Book Management: add_book(), get_book(), search_books_by_*
  - User Management: add_user(), get_user(), get_all_users()
  - Transaction Management: borrow_book(), return_book(), get_overdue_books()
  - Statistics: get_library_statistics()
- **Key Concepts**: Composition, data structure management, business logic

## Borrowing Limits by User Type

| User Type | Limit |
|-----------|-------|
| Student   | 5     |
| Faculty   | 10    |
| Staff     | 7     |
| Visitor   | 2     |

## Fine Calculation
- **Fine Rate**: Rs. 10 per day
- **Borrowing Period**: 14 days (default)
- Fines are automatically calculated when books are returned late

## Usage Example

```python
from models import Library, Book, User
from models.user import UserType

# Create a library
library = Library("Central Library", "New Delhi")

# Add a book
library.add_book("ISBN001", "Python Programming", "Guido van Rossum", "Programming", 2020, 3)

# Register a user
library.add_user("U001", "Kartik Singh", "kartik@email.com", "9876543210", UserType.STUDENT)

# Borrow a book
success, message = library.borrow_book("U001", "ISBN001")
print(message)

# Return a book
success, message, fine = library.return_book("U001", "ISBN001")
print(message)

# Get library statistics
stats = library.get_library_statistics()
print(stats)
```

## Running the Demo

```bash
python main.py
```

This will run a comprehensive demonstration of all features including:
- Creating a library
- Adding books and users
- Borrowing and returning books
- Searching for books
- Displaying statistics

## Learning Resources

This project helps understand:
- **Encapsulation**: How to hide internal data and expose through properties
- **Composition**: How to combine multiple classes into a larger system
- **Data Validation**: Input validation and error handling
- **Enum Usage**: Using enumerations for type safety
- **Design Patterns**: Composition pattern for system design
- **Business Logic**: Implementing real-world requirements

## Future Enhancements

- Add database persistence (SQLite/SQL)
- Implement user authentication
- Add reservation system for books
- Email notifications for overdue books
- Generate reports and analytics
- Implement inheritance hierarchy for specialized user types
- Add fine payment tracking
- Implement a web interface using Flask/Django

## Author

Created for learning Object-Oriented Programming concepts in Python.

## License

Open source - Use freely for educational purposes.
