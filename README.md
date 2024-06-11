This Python code implements a simple library management system that allows you to:

Create and manage books (title, author, ISBN, price)
Create and manage library members (ID, name, age, email)
Add books to the library
Add members to the library
View all available books in the library
Borrow books by members (checks for member and book existence, availability)
Return borrowed books (checks for member, book, and borrowing validity)
Classes:

Book
Represents a book in the library system.
Attributes:
title (str): Title of the book.
author_name (str): Name of the author.
ISBN (str): ISBN number of the book.
price (float): Price of the book.
Methods:
__init__(self, title, author_name, ISBN, price): Initializes a Book object.
@property title(self): Getter for title.
@property author_name(self): Getter for author_name.
@property ISBN(self): Getter for ISBN.
@property price(self): Getter for price.
__repr__(self): String representation of the Book object.
Member
Represents a member of the library system.
Attributes:
ID (int): Unique ID of the member.
name (str): Name of the member.
age (int): Age of the member.
email (str): Email address of the member.
Methods:
__init__(self, ID, name, age, email): Initializes a Member object.
@property ID(self): Getter for ID.
@property name(self): Getter for name.
@property age(self): Getter for age.
@property email(self): Getter for email.
__repr__(self): String representation of the Member object.
Library
Represents the library itself.
Attributes:
__books (dict): Dictionary of books with ISBN as keys and Book objects as values.
__members (dict): Dictionary of members with ID as keys and Member objects as values.
__borrowed_books (dict): Dictionary of borrowed books with ISBN as keys and member ID (who borrowed it) as values.
Methods:
__init__(self): Initializes a Library object.
add_book(self, book): Adds a Book object to the library (checks for duplicate ISBN).
add_member(self, member): Adds a Member object to the library (checks for duplicate ID).
show_all_books(self): Prints information about all available books in the library.
borrow_book(self, member_id, book_isbn): Allows a member to borrow a book (checks for member, book existence, and availability).
return_book(self, member_id, book_isbn): Allows a member to return a borrowed book (checks for member, book, and borrowing validity).
main Function:

Creates a Library object.
Creates two Book objects and adds them to the library.
Creates two Member objects and adds them to the library.
Demonstrates functionalities by showing all books, borrowing and returning a book.
Usage:

Save the code as a Python file (e.g., library_management.py).
Run the script from the command line: python library_management.py
Error Handling:

The code includes error handling using ValueError exceptions to prevent unexpected behavior:

Adding duplicate books or members (by ISBN or ID)
Borrowing non-existent or unavailable books
Returning a book that wasn't borrowed or by a different member
