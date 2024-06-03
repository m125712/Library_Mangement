class Book:
    def __init__(self,title:str,author_name:str,ISBN:str, price:float):
        assert  price >=0 ,"price should greater than 0"
        self.title=title
        self.author_name=author_name
        self.ISBN=ISBN
        self.price=price
    def __repr__(self):
        return f"Book('{self.title}','{self.author_name}','{self.ISBN}',{self.price})"
    
class Member:
    def __init__(self,ID:int,name:str,age:int,email:str):
        assert  age >=0 ,"age should greater than 0"
        self.ID=ID
        self.name=name
        self.age=age
        self.email=email
    def __repr__(self):
        return f"Book({self.ID},'{self.name}','{self.age}','{self.email}')"
        
class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.borrowed_books = {}

    def add_book(self, book: Book):
        if book.ISBN in self.books:
            raise ValueError(f"A book with ISBN '{book.ISBN}' already exists in the library.")
        self.books[book.ISBN] = book

    def add_member(self, member: Member):
        if member.ID in self.members:
            raise ValueError(f"A member with ID {member.ID} already exists in the library.")
        self.members[member.ID] = member
    def show_all_books(self):

        if not self.books:
            print("There are currently no books in the library.")
        else:
            print("** Books in Library **")
            for isbn, book in self.books.items():
                print(f"ISBN: {isbn}")
                print(f"Title: {book.title}")
                print(f"Author: {book.author_name}")
                print(f"Price: ${book.price:.2f}") 
                print("-" * 20)  

def main():
  
  library = Library()

  
  book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", "9780261102694", 25.99)
  book2 = Book("Pride and Prejudice", "Jane Austen", "9780140439516", 14.95)
  book3 = Book("Pride and Prejudice", "Jane Austen", "9780140439516", 14.95)
  library.add_book(book1)
  library.add_book(book2)

  
  member1 = Member(123, "Alice Smith", 30, "alice.smith@email.com")
  member2 = Member(456, "Bob Jones", 25, "bob.jones@email.com")
  library.add_member(member1)
  library.add_member(member2)

 
 
  library.show_all_books()


 

if __name__ == "__main__":
  main()