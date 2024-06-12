# A library system that allows members to borrow books and return them.

class Book():
    def __init__(self, title, author, genre, year, available=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.available = available

    def __str__(self):
        return f'{self.title} by {self.author}'
    

class Member():
    def __init__(self, name, age, member_id, borrowed_books=[]):
        self.name = name
        self.age = age
        self.member_id = member_id
        self.borrowed_books = borrowed_books

    def __str__(self):
        return f'{self.name} with ID: {self.member_id}'
    
    
class Library():
    def __init__(self, name, books=[], members=[]):
        self.name = name
        self.books = books
        self.members = members

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, book, member):
        if book.available:
            book.available = False
            member.borrowed_books.append(book)
            print(f'{member.name} has borrowed {book.title}.')
        else:
            print(f'{book.title} is not available.')

    def return_book(self, book, member):
        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print(f'{member.name} has returned {book.title}.')
        else:
            print(f'{member.name} did not borrow {book.title}.')

    def __str__(self):
        return f'{self.name} library with {len(self.books)} books and {len(self.members)} members.'
    

# Create books
book1 = Book('Harry Potter', 'J.K. Rowling', 'Fantasy', 1997)

book2 = Book('The Da Vinci Code', 'Dan Brown', 'Mystery', 2003)

book3 = Book('The Alchemist', 'Paulo Coelho', 'Fiction', 1988)

# Create members
member1 = Member('Alice', 25, 1)

member2 = Member('Bob', 30, 2)

# Create library
library = Library('Central Library')

# Add books to library
library.add_book(book1)

library.add_book(book2)

library.add_book(book3)

# Add members to library
library.add_member(member1)

library.add_member(member2)

# Borrow books
library.borrow_book(book1, member1)

library.borrow_book(book2, member2)

library.borrow_book(book3, member1)

# Return books
library.return_book(book1, member1)

library.return_book(book2, member2)

library.return_book(book3, member1)

print(library)

# Output:
# Alice has borrowed Harry Potter.
# Bob has borrowed The Da Vinci Code.
# Alice has borrowed The Alchemist.
# Alice has returned Harry Potter.
# Bob has returned The Da Vinci Code.
# Alice has returned The Alchemist.
# Central Library library with 3 books and 2 members.

