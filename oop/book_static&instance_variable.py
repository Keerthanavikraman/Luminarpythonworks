
#2 types of variables
#1...static variable...related to class...accessed using class name
#2...instance variable...related to methods...accessed called using self


# class Book:            #variables defined inside the class called static variable
#     def setval(self,book_name,author,pages,library_name):
#         self.book_name=book_name
#         self.author=author
#         self.pages=pages
#         self.library_name=library_name
#     def printval(self):
#         print(self.book_name,self.author,self.pages,self.library_name)
# book1=Book()
# book1.setval("lords of meluha","amish",200,"great_library")
# book1.printval()
#
# book2=Book()
# book2.setval("half girlfriend","chetan bhagat",250,"town_library")
# book2.printval()


class Book:            #variables defined inside the class called static variable
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