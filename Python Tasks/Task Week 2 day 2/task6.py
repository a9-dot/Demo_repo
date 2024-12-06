class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
        else:
            raise Exception("Book is already borrowed.")

    def return_book(self):
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                book.borrow()
                return
        raise Exception("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                return
        raise Exception("Book not found.")

# Example usage
library = Library()
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
library.add_book(book1)
library.add_book(book2)

library.borrow_book("1984")
print(book1.is_borrowed)  # Output: True
library.return_book("1984")
print(book1.is_borrowed)  # Output: False
