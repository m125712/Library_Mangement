class Book:
    def __init__(self,title:str,author_name:str,ISBN:str, price:float):
        assert  price >=0 ,"price should greater than 0"
        self.__title=title
        self.__author_name=author_name
        self.__ISBN=ISBN
        self.__price=price
    @property
    def title(self):
        return self.__title

    @property
    def author_name(self):
        return self.__author_name

    @property
    def ISBN(self):
        return self.__ISBN

    @property
    def price(self):
        return self.__price
    def __repr__(self):
        return f"Book('{self.title}','{self.author_name}','{self.ISBN}',{self.price})"
    
class Member:
    def __init__(self,ID:int,name:str,age:int,email:str):
        assert  age >=0 ,"age should greater than 0"
        self.__ID=ID
        self.__name=name
        self.__age=age
        self.__email=email
    @property
    def ID(self):
        return self.__ID
    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age

    @property
    def email(self):
        return self.__email
        return self.__price
    def __repr__(self):
        return f"Book({self.ID},'{self.name}','{self.age}','{self.email}')"
        
class Library:
    def __init__(self):
        self.__books = {}
        self.__members = {}
        self.__borrowed_books = {}

    def add_book(self, book: Book):
        if book.ISBN in self.__books:
            raise ValueError(f"A book with ISBN '{book.ISBN}' already exists in the library.")
        self.__books[book.ISBN] = book

    def add_member(self, member: Member):
        if member.ID in self.__members:
            raise ValueError(f"A member with ID {member.ID} already exists in the library.")
        self.__members[member.ID] = member
    def show_all_books(self):

        if not self.__books:
            print("There are currently no books in the library.")
        else:
            print("** Books in Library **")
            for isbn, book in self.__books.items():
                print(f"ISBN: {isbn}")
                print(f"Title: {book.title}")
                print(f"Author: {book.author_name}")
                print(f"Price: ${book.price:.2f}") 
                print("-" * 20) 
    def borrow_book(self, member_id: int, book_isbn: str):
        if member_id not in self.__members:
            raise ValueError(f"Member with ID {member_id} is not a member of the library.")
            
        if book_isbn not in self.__books:
            raise ValueError(f"Book with ISBN {book_isbn} is not available in the library.")
         
        if book_isbn in self.__borrowed_books:
            raise ValueError(f"Book with ISBN {book_isbn} is already borrowed by someone.")
            
        self.__borrowed_books[book_isbn] = member_id
        print(f"Book with ISBN {book_isbn} is successfully borrowed by member with ID {member_id}.")

    def return_book(self, member_id: int, book_isbn: str):
        if member_id not in self.__members:
            raise ValueError(f"Member with ID {member_id} is not a member of the library.")
            return
        if book_isbn not in self.__borrowed_books:
            raise ValueError(f"Book with ISBN {book_isbn} is not borrowed from the library.")
            return
        if self.__borrowed_books[book_isbn] != member_id:
            raise ValueError(f"Book with ISBN {book_isbn} is not borrowed by member with ID {member_id}.")
            return
        del self.__borrowed_books[book_isbn]
        print(f"Book with ISBN {book_isbn} is successfully returned by member with ID {member_id}.")

def main():
  
    library = Library()

  
    book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", "9780261102694", 25.99)
    book2 = Book("Pride and Prejudice", "Jane Austen", "9780140439516", 14.95)
    library.add_book(book1)
    library.add_book(book2)

  
    member1 = Member(123, "Alice Smith", 30, "alice.smith@email.com")
    member2 = Member(456, "Bob Jones", 25, "bob.jones@email.com")
    library.add_member(member1)
    library.add_member(member2)
    
 
 
    library.show_all_books()
    library.borrow_book(123, "9780261102694")
    library.return_book(123, "9780261102694") 

 

if __name__ == "__main__":
  main()
