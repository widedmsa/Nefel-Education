class Book :
    def __init__(self,title,author,year,genre) :
        self.title= title
        self.author=author
        self.year=year
        self.genre=genre
        self.is_checked_out=False #default value for check out status 

    def check_out(self) :
        #set the book status 
        self.is_checked_out=True

    def return_book(self) :
        #set the book status to available 
        self.is_checked_out=False 

    def display_info(self) :
        #print the details of the book including its status 
        if self.is_checked_out == True :
            status = "Checked out"
        else : 
            status = "Available"
        print(f"The book's title is {self.title} , is a {self.genre} book , its author is {self.author} , it was realeased in {self.year} ,  and it's currently {status} ")
