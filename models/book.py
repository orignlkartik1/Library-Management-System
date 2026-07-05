"""
Book class - Represents a book in the library
Demonstrates: Encapsulation, Properties, String representation
"""

class Book:
    """Represents a book with details like ISBN, title, author, etc."""
    
    # Class variable to track total books created
    total_books = 0
    
    def __init__(self, isbn, title, author, genre, publication_year, quantity=1):
        """
        Initialize a Book object.
        
        Args:
            isbn (str): Unique identifier for the book
            title (str): Title of the book
            author (str): Author of the book
            genre (str): Genre of the book
            publication_year (int): Year of publication
            quantity (int): Number of copies available (default: 1)
        """
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_year = publication_year
        self.__quantity = quantity
        self.__available_quantity = quantity
        Book.total_books += 1
    
    # Properties with getters and setters (Encapsulation)
    @property
    def isbn(self):
        """Get the ISBN of the book."""
        return self.__isbn
    
    @property
    def title(self):
        """Get the title of the book."""
        return self.__title
    
    @property
    def author(self):
        """Get the author of the book."""
        return self.__author
    
    @property
    def genre(self):
        """Get the genre of the book."""
        return self.__genre
    
    @property
    def publication_year(self):
        """Get the publication year of the book."""
        return self.__publication_year
    
    @property
    def quantity(self):
        """Get the total quantity of this book."""
        return self.__quantity
    
    @property
    def available_quantity(self):
        """Get the available (not borrowed) quantity of this book."""
        return self.__available_quantity
    
    @available_quantity.setter
    def available_quantity(self, value):
        """Set the available quantity (with validation)."""
        if value < 0 or value > self.__quantity:
            raise ValueError(f"Available quantity must be between 0 and {self.__quantity}")
        self.__available_quantity = value
    
    def borrow(self):
        """
        Reduce available quantity when a book is borrowed.
        
        Returns:
            bool: True if successful, False if no copies available
        """
        if self.__available_quantity > 0:
            self.__available_quantity -= 1
            return True
        return False
    
    def return_book(self):
        """
        Increase available quantity when a book is returned.
        
        Returns:
            bool: True if successful, False if already at maximum
        """
        if self.__available_quantity < self.__quantity:
            self.__available_quantity += 1
            return True
        return False
    
    def __str__(self):
        """String representation of the book."""
        return f"{self.__title} by {self.__author} (ISBN: {self.__isbn})"
    
    def __repr__(self):
        """Detailed representation of the book."""
        return (f"Book(isbn='{self.__isbn}', title='{self.__title}', "
                f"author='{self.__author}', genre='{self.__genre}', "
                f"year={self.__publication_year}, available={self.__available_quantity}/{self.__quantity})")
    
    def get_book_details(self):
        """Get detailed information about the book."""
        return {
            'isbn': self.__isbn,
            'title': self.__title,
            'author': self.__author,
            'genre': self.__genre,
            'publication_year': self.__publication_year,
            'total_quantity': self.__quantity,
            'available_quantity': self.__available_quantity
        }