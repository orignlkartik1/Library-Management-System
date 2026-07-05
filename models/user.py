"""
User class - Represents a library user/member
Demonstrates: Encapsulation, Inheritance hierarchy preparation, Data validation
"""

from datetime import datetime
from enum import Enum

class UserType(Enum):
    """Enum for different types of users."""
    STUDENT = "student"
    FACULTY = "faculty"
    STAFF = "staff"
    VISITOR = "visitor"


class User:
    """Represents a library user/member."""
    
    # Class variable to track total users
    total_users = 0
    
    def __init__(self, user_id, name, email, phone, user_type=UserType.STUDENT):
        """
        Initialize a User object.
        
        Args:
            user_id (str): Unique identifier for the user
            name (str): Full name of the user
            email (str): Email address
            phone (str): Phone number
            user_type (UserType): Type of user (default: STUDENT)
        """
        self.__user_id = user_id
        self.__name = self._validate_name(name)
        self.__email = self._validate_email(email)
        self.__phone = phone
        self.__user_type = user_type
        self.__membership_date = datetime.now()
        self.__borrowed_books = []  # List to track borrowed books
        self.__is_active = True
        User.total_users += 1
    
    @staticmethod
    def _validate_name(name):
        """Validate and return user name."""
        if not name or len(name.strip()) == 0:
            raise ValueError("Name cannot be empty")
        return name.strip()
    
    @staticmethod
    def _validate_email(email):
        """Validate and return email address."""
        if '@' not in email or '.' not in email:
            raise ValueError("Invalid email format")
        return email.lower()
    
    # Properties
    @property
    def user_id(self):
        """Get the user ID."""
        return self.__user_id
    
    @property
    def name(self):
        """Get the user's name."""
        return self.__name
    
    @property
    def email(self):
        """Get the user's email."""
        return self.__email
    
    @property
    def phone(self):
        """Get the user's phone number."""
        return self.__phone
    
    @property
    def user_type(self):
        """Get the user type."""
        return self.__user_type
    
    @property
    def borrowed_books(self):
        """Get the list of borrowed books."""
        return self.__borrowed_books.copy()
    
    @property
    def is_active(self):
        """Check if the user is active."""
        return self.__is_active
    
    @property
    def borrowed_count(self):
        """Get the number of books currently borrowed."""
        return len(self.__borrowed_books)
    
    @property
    def membership_date(self):
        """Get the membership date."""
        return self.__membership_date
    
    def get_borrowing_limit(self):
        """
        Get the maximum number of books this user can borrow.
        Different limits for different user types.
        """
        limits = {
            UserType.STUDENT: 5,
            UserType.FACULTY: 10,
            UserType.STAFF: 7,
            UserType.VISITOR: 2
        }
        return limits.get(self.__user_type, 3)
    
    def can_borrow(self):
        """Check if user can borrow more books."""
        return self.__is_active and self.borrowed_count < self.get_borrowing_limit()
    
    def add_borrowed_book(self, book_isbn):
        """
        Add a book to the user's borrowed list.
        
        Args:
            book_isbn (str): ISBN of the borrowed book
            
        Returns:
            bool: True if successful, False if limit reached or inactive
        """
        if not self.can_borrow():
            return False
        self.__borrowed_books.append(book_isbn)
        return True
    
    def remove_borrowed_book(self, book_isbn):
        """
        Remove a book from the user's borrowed list.
        
        Args:
            book_isbn (str): ISBN of the book to return
            
        Returns:
            bool: True if successful, False if book not in list
        """
        if book_isbn in self.__borrowed_books:
            self.__borrowed_books.remove(book_isbn)
            return True
        return False
    
    def deactivate(self):
        """Deactivate the user account."""
        self.__is_active = False
    
    def activate(self):
        """Activate the user account."""
        self.__is_active = True
    
    def __str__(self):
        """String representation of the user."""
        return f"{self.__name} ({self.__user_id})"
    
    def __repr__(self):
        """Detailed representation of the user."""
        return (f"User(id='{self.__user_id}', name='{self.__name}', "
                f"email='{self.__email}', type={self.__user_type.value}, "
                f"borrowed={self.borrowed_count}/{self.get_borrowing_limit()})")
    
    def get_user_details(self):
        """Get detailed information about the user."""
        return {
            'user_id': self.__user_id,
            'name': self.__name,
            'email': self.__email,
            'phone': self.__phone,
            'user_type': self.__user_type.value,
            'is_active': self.__is_active,
            'borrowed_books': self.__borrowed_books.copy(),
            'borrowed_count': self.borrowed_count,
            'borrowing_limit': self.get_borrowing_limit(),
            'membership_date': self.__membership_date.strftime('%Y-%m-%d %H:%M:%S')
        }