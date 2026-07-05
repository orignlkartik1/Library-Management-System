"""
Library class - Main class to manage the entire library system
Demonstrates: Composition, Data structure management, Business logic
"""

from .book import Book
from .user import User
from .transaction import Transaction, TransactionType


class Library:
    """
    Manages the entire library system including books, users, and transactions.
    Demonstrates composition and overall system management.
    """
    
    def __init__(self, name, location):
        """
        Initialize a Library object.
        
        Args:
            name (str): Name of the library
            location (str): Physical location of the library
        """
        self.__name = name
        self.__location = location
        self.__books = {}  # Dictionary: ISBN -> Book object
        self.__users = {}  # Dictionary: User ID -> User object
        self.__transactions = []  # List of transactions
    
    # Properties
    @property
    def name(self):
        """Get the library name."""
        return self.__name
    
    @property
    def location(self):
        """Get the library location."""
        return self.__location
    
    @property
    def total_books_count(self):
        """Get total number of unique books in the library."""
        return len(self.__books)
    
    @property
    def total_members(self):
        """Get total number of active members."""
        return len([u for u in self.__users.values() if u.is_active])
    
    # Book Management Methods
    def add_book(self, isbn, title, author, genre, publication_year, quantity=1):
        """
        Add a new book to the library.
        
        Args:
            isbn (str): Unique ISBN
            title (str): Book title
            author (str): Author name
            genre (str): Book genre
            publication_year (int): Year of publication
            quantity (int): Number of copies (default: 1)
            
        Returns:
            bool: True if successful, False if ISBN already exists
        """
        if isbn in self.__books:
            return False
        
        book = Book(isbn, title, author, genre, publication_year, quantity)
        self.__books[isbn] = book
        return True
    
    def get_book(self, isbn):
        """
        Get a book by ISBN.
        
        Args:
            isbn (str): Book ISBN
            
        Returns:
            Book: Book object if found, None otherwise
        """
        return self.__books.get(isbn)
    
    def search_books_by_title(self, title):
        """
        Search books by title (partial match, case-insensitive).
        
        Args:
            title (str): Search title
            
        Returns:
            list: List of matching Book objects
        """
        title_lower = title.lower()
        return [book for book in self.__books.values() 
                if title_lower in book.title.lower()]
    
    def search_books_by_author(self, author):
        """
        Search books by author (partial match, case-insensitive).
        
        Args:
            author (str): Author name
            
        Returns:
            list: List of matching Book objects
        """
        author_lower = author.lower()
        return [book for book in self.__books.values() 
                if author_lower in book.author.lower()]
    
    def search_books_by_genre(self, genre):
        """
        Search books by genre.
        
        Args:
            genre (str): Genre name
            
        Returns:
            list: List of matching Book objects
        """
        genre_lower = genre.lower()
        return [book for book in self.__books.values() 
                if genre_lower in book.genre.lower()]
    
    def get_available_books(self):
        """
        Get all books with available copies.
        
        Returns:
            list: List of Book objects with available_quantity > 0
        """
        return [book for book in self.__books.values() 
                if book.available_quantity > 0]
    
    # User Management Methods
    def add_user(self, user_id, name, email, phone, user_type):
        """
        Register a new user in the library.
        
        Args:
            user_id (str): Unique user ID
            name (str): User's full name
            email (str): Email address
            phone (str): Phone number
            user_type: User type from UserType enum
            
        Returns:
            bool: True if successful, False if user ID already exists
        """
        if user_id in self.__users:
            return False
        
        user = User(user_id, name, email, phone, user_type)
        self.__users[user_id] = user
        return True
    
    def get_user(self, user_id):
        """
        Get a user by ID.
        
        Args:
            user_id (str): User ID
            
        Returns:
            User: User object if found, None otherwise
        """
        return self.__users.get(user_id)
    
    def get_all_users(self, active_only=True):
        """
        Get all users.
        
        Args:
            active_only (bool): If True, return only active users (default: True)
            
        Returns:
            list: List of User objects
        """
        if active_only:
            return [u for u in self.__users.values() if u.is_active]
        return list(self.__users.values())
    
    # Transaction Management Methods
    def borrow_book(self, user_id, isbn):
        """
        Process a book borrowing transaction.
        
        Args:
            user_id (str): ID of the borrowing user
            isbn (str): ISBN of the book to borrow
            
        Returns:
            tuple: (success: bool, message: str)
        """
        user = self.get_user(user_id)
        if not user:
            return False, "User not found"
        
        book = self.get_book(isbn)
        if not book:
            return False, "Book not found"
        
        if not user.can_borrow():
            return False, f"User has reached borrowing limit ({user.get_borrowing_limit()} books)"
        
        if not book.borrow():
            return False, "Book is not available"
        
        # Record transaction
        user.add_borrowed_book(isbn)
        transaction = Transaction(user_id, isbn, TransactionType.BORROW)
        self.__transactions.append(transaction)
        
        return True, f"Book '{book.title}' successfully borrowed by {user.name}"
    
    def return_book(self, user_id, isbn):
        """
        Process a book return transaction.
        
        Args:
            user_id (str): ID of the returning user
            isbn (str): ISBN of the book to return
            
        Returns:
            tuple: (success: bool, message: str, fine: float)
        """
        user = self.get_user(user_id)
        if not user:
            return False, "User not found", 0
        
        book = self.get_book(isbn)
        if not book:
            return False, "Book not found", 0
        
        if not user.remove_borrowed_book(isbn):
            return False, "User has not borrowed this book", 0
        
        book.return_book()
        
        # Find the borrow transaction and create a return transaction
        borrow_transaction = None
        for trans in self.__transactions:
            if (trans.user_id == user_id and trans.book_isbn == isbn and 
                trans.transaction_type == TransactionType.BORROW and 
                trans.return_date is None):
                borrow_transaction = trans
                break
        
        if borrow_transaction:
            borrow_transaction.process_return()
            fine = borrow_transaction.fine
            message = f"Book '{book.title}' successfully returned by {user.name}"
            if fine > 0:
                message += f". Fine: Rs. {fine}"
            return True, message, fine
        
        return True, f"Book '{book.title}' successfully returned by {user.name}", 0
    
    def get_overdue_books(self):
        """
        Get all currently overdue books.
        
        Returns:
            list: List of Transaction objects for overdue books
        """
        return [t for t in self.__transactions 
                if t.transaction_type == TransactionType.BORROW and t.is_overdue()]
    
    def get_user_transactions(self, user_id):
        """
        Get all transactions for a specific user.
        
        Args:
            user_id (str): User ID
            
        Returns:
            list: List of Transaction objects
        """
        return [t for t in self.__transactions if t.user_id == user_id]
    
    # Library Statistics
    def get_library_statistics(self):
        """
        Get overall library statistics.
        
        Returns:
            dict: Library statistics
        """
        total_available = sum(b.available_quantity for b in self.__books.values())
        total_borrowed = sum(b.quantity - b.available_quantity for b in self.__books.values())
        
        return {
            'library_name': self.__name,
            'location': self.__location,
            'total_unique_books': len(self.__books),
            'total_book_copies': sum(b.quantity for b in self.__books.values()),
            'total_available_copies': total_available,
            'total_borrowed_copies': total_borrowed,
            'total_members': self.total_members,
            'total_transactions': len(self.__transactions),
            'overdue_books': len(self.get_overdue_books())
        }
    
    def __str__(self):
        """String representation of the library."""
        return f"{self.__name} - {self.__location}"
    
    def __repr__(self):
        """Detailed representation of the library."""
        return (f"Library(name='{self.__name}', location='{self.__location}', "
                f"books={len(self.__books)}, members={self.total_members})")