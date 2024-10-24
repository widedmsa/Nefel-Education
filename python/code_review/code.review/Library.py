from Book import Book
class Library : 
    def __init__(self,name) :
        self.name = name
        self.books = []

    def add_book(self,book) :
        #check if book is an instance of the class book 
        if isinstance(book,Book):
            #add a Book instance to the library collection 
            self.books.append(book)
        else : 
            print("Sorry it's not a book")


    def list_books(self) :
        #loop through the books in the library and display their info 
        print(f"\n Books in {self.name} :")
        for book in self.books:
            book.display_info()


    def find_book(self,title) :
        #return thebook that matches the given title or return false if not found 
        for book in self.books :
            if book.title.lower() == title() :
                return book #return the found book
        print("book not found")
        return False # return false if the book is not found 
