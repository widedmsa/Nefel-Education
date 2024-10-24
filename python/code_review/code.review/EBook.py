from Book import Book
class EBook(book) :
    def __init__(self,title,author,year,genre,file_size):
    #initialiwze the ebook attributes ay haja mta3 lparent 
    super().__init__(title,author,year,genre)
    self.file_size=file_size


    def display_info(self) :
        #print the details of the book including its status 
        if self.is_checked_out == True :
            status = "Checked out"
        else : 
            status = "Available"
        print(f"The book's title is {self.title} , is a {self.genre} book , its author is {self.author} , it was realeased in {self.year} ,  and it's currently {status},File size : {self.file_size} ")