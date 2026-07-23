class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, title, author, copies):
        self.books[title] = Book(title, author, copies)

    def register_patron(self, name):
        self.patrons[name] = Patron(name)

    def borrow_book(self, patron_name, title):
        if patron_name not in self.patrons:
            print("Patron not found")
            return

        if title not in self.books:
            print("Book not found")
            return

        if self.books[title].copies == 0:
            print("Book is not available")
            return

        self.patrons[patron_name].borrowed_books.append(title)
        self.books[title].copies -= 1
        print(f"{patron_name} borrowed {title}")

    def return_book(self, patron_name, title):
        if patron_name not in self.patrons:
            print("Patron not found")
            return

        if title not in self.patrons[patron_name].borrowed_books:
            print("This book was not borrowed by this patron")
            return

        self.patrons[patron_name].borrowed_books.remove(title)
        self.books[title].copies += 1
        print(f"{patron_name} returned {title}")


library = Library()
library.add_book("Python Basics", "John", 2)
library.add_book("OOP in Python", "Alice", 1)
library.register_patron("Sam")
library.register_patron("Ria")

library.borrow_book("Sam", "Python Basics")
library.borrow_book("Ria", "OOP in Python")
library.return_book("Sam", "Python Basics")