
#create a Book with instance library_name,book_name,author,pages

class Book:
    library_name="town_library"
    def setval(self,book_name,author,pages):
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def printval(self):
        print(self.book_name,self.author,self.pages,Book.library_name)
book1=Book()
book1.setval("lords of meluha","amish",200)
book1.printval()

book2=Book()
book2.setval("half girlfriend","chetan bhagat",250)
book2.printval()