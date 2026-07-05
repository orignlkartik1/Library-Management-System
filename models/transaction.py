"""
Transaction class - Represents a book borrow/return transaction
Demonstrates: Encapsulation, Datetime handling, Transaction tracking
"""

from datetime import datetime, timedelta
from enum import Enum


class TransactionType(Enum):
    """Enum for transaction types."""
    BORROW = "borrow"
    RETURN = "return"


class Transaction:
    """Represents a book transaction (borrow or return)."""
    
    # Class variable to track all transactions
    all_transactions = []
    
    def __init__(self, user_id, book_isbn, transaction_type, due_days=14):
        """
        Initialize a Transaction object.
        
        Args:
            user_id (str): ID of the user
            book_isbn (str): ISBN of the book
            transaction_type (TransactionType): Type of transaction
            due_days (int): Days until due (default: 14 days)
        """
        self.__user_id = user_id
        self.__book_isbn = book_isbn
        self.__transaction_type = transaction_type
        self.__transaction_date = datetime.now()
        self.__due_date = None
        self.__return_date = None
        self.__fine = 0.0
        
        if transaction_type == TransactionType.BORROW:
            self.__due_date = self.__transaction_date + timedelta(days=due_days)
        
        Transaction.all_transactions.append(self)
    
    # Properties
    @property
    def user_id(self):
        """Get the user ID."""
        return self.__user_id
    
    @property
    def book_isbn(self):
        """Get the book ISBN."""
        return self.__book_isbn
    
    @property
    def transaction_type(self):
        """Get the transaction type."""
        return self.__transaction_type
    
    @property
    def transaction_date(self):
        """Get the transaction date."""
        return self.__transaction_date
    
    @property
    def due_date(self):
        """Get the due date (for borrow transactions)."""
        return self.__due_date
    
    @property
    def return_date(self):
        """Get the return date (for return transactions)."""
        return self.__return_date
    
    @property
    def fine(self):
        """Get the fine amount."""
        return self.__fine
    
    def is_overdue(self):
        """
        Check if the borrowed book is overdue.
        
        Returns:
            bool: True if overdue and not yet returned
        """
        if self.__transaction_type != TransactionType.BORROW:
            return False
        if self.__return_date is not None:
            return False  # Already returned
        return datetime.now() > self.__due_date
    
    def get_days_overdue(self):
        """
        Get the number of days overdue.
        
        Returns:
            int: Days overdue (0 if not overdue)
        """
        if not self.is_overdue():
            return 0
        return (datetime.now() - self.__due_date).days
    
    def process_return(self):
        """
        Process the return of a borrowed book and calculate fine if overdue.
        Fine: Rs. 10 per day (can be customized)
        """
        if self.__transaction_type != TransactionType.BORROW:
            raise ValueError("Can only return borrowed books")
        
        if self.__return_date is not None:
            raise ValueError("Book already returned")
        
        self.__return_date = datetime.now()
        days_overdue = self.get_days_overdue()
        
        if days_overdue > 0:
            self.__fine = days_overdue * 10  # Rs. 10 per day
    
    def waive_fine(self):
        """Waive the fine for this transaction."""
        self.__fine = 0.0
    
    def __str__(self):
        """String representation of the transaction."""
        if self.__transaction_type == TransactionType.BORROW:
            status = "BORROWED" if self.__return_date is None else "RETURNED"
            return f"{status}: User {self.__user_id} - Book {self.__book_isbn}"
        return f"RETURN: User {self.__user_id} - Book {self.__book_isbn}"
    
    def __repr__(self):
        """Detailed representation of the transaction."""
        return (f"Transaction(user='{self.__user_id}', book='{self.__book_isbn}', "
                f"type={self.__transaction_type.value}, date={self.__transaction_date.strftime('%Y-%m-%d')}, "
                f"fine={self.__fine})")
    
    def get_transaction_details(self):
        """Get detailed information about the transaction."""
        return {
            'user_id': self.__user_id,
            'book_isbn': self.__book_isbn,
            'transaction_type': self.__transaction_type.value,
            'transaction_date': self.__transaction_date.strftime('%Y-%m-%d %H:%M:%S'),
            'due_date': self.__due_date.strftime('%Y-%m-%d') if self.__due_date else None,
            'return_date': self.__return_date.strftime('%Y-%m-%d %H:%M:%S') if self.__return_date else None,
            'is_overdue': self.is_overdue(),
            'days_overdue': self.get_days_overdue(),
            'fine': self.__fine
        }
    
    @classmethod
    def get_all_transactions(cls):
        """Get all transactions."""
        return cls.all_transactions.copy()
    
    @classmethod
    def get_user_transactions(cls, user_id):
        """Get all transactions for a specific user."""
        return [t for t in cls.all_transactions if t.user_id == user_id]
    
    @classmethod
    def get_overdue_books(cls):
        """Get all currently overdue books."""
        return [t for t in cls.all_transactions if t.is_overdue()]