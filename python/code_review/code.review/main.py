from Library import Library
from Book import Book
from EBook import EBook


my_library= Library("City library") # creating a library instance
book1= Book("The tempest" , "William Shakespeare", 1745,"Drama",6)
book2=EBook("The house of thunder","Dean Koontz",1995,"Thriller",5)
my_library.add_book(book1)
my_library.add_book(book2)

my_library.list_books()
book1.check_out()
book2.check_out()
book1.return_book()
my_library.list_books()


#find a specific book
found_book = my_library.find_book("The tempest")
if found_book :
    found_book.display_info()