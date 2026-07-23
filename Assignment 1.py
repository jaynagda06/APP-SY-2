class Book:
    
  def __init__(self, title, author, copies):
    self.title = title
    self.author = author
    self.copies = copies


class User:

  def __init__(self, name):
    self.name = name
    self.borrowed_books = []

  def borrow(self, title):
    self.borrowed_books.append(title)

  def return_book(self, title):
    self.borrowed_books.remove(title)


class Library:

  def __init__(self):
    self.books = {}
    self.users = {}  # Fixed naming consistency

  def add_book(self, title, author, copies):
    self.books[title] = Book(title, author, copies)

  def register_user(self, name):
    self.users[name] = User(name)

  def borrow_book(self, user_name, title):
    if user_name not in self.users:
      print("User not found")
      return
    if title not in self.books:
      print("Book not found")
      return
    if self.books[title].copies == 0:
      print("Book is not available")
      return

    self.users[user_name].borrow(title)
    self.books[title].copies -= 1
    print(f"{user_name} borrowed {title}")

  def return_book(self, user_name, title):
    if user_name not in self.users:
      print("User not found")
      return
    if title not in self.users[user_name].borrowed_books:
      print("This book was not borrowed by this user")
      return

    self.users[user_name].return_book(title)
    self.books[title].copies += 1
    print(f"{user_name} returned {title}")



library = Library()
library.add_book("Python Basics", "John", 2)
library.add_book("OOP in Python", "Alice", 1)

library.register_user("Sam")
library.register_user("Ria")

library.borrow_book("Sam", "Python Basics")
library.borrow_book("Ria", "OOP in Python")
library.return_book("Sam", "Python Basics")
