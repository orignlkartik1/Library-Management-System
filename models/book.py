class Book:

    def __init__(self,title:str,author:str,total_copies:int,):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow(self)->bool:
        if(self.is_available()):
            self.available_copies-=1
            return True
        else:
            return False

    def return_book(self)->None:
        if self.available_copies < self.total_copies:
            self.available_copies+=1

    def is_available(self)->bool:
        return self.available_copies>0

    def __str__(self) -> str:
        """
        User-friendly representation.
        """

        return (
            f"Title      : {self.title}\n"
            f"Author     : {self.author}\n"
            f"Available  : {self.available_copies}/{self.total_copies}"
        )

    def __repr__(self) -> str:
        return (
            f"Book(title={self.title!r}, "
            f"author={self.author!r}, "
        )