books={
"alchemist":{"book_name":"alchemist","author":"paulo","price":200,"av_copies":100,"sold":10}
"halfgirlfriend":{"book_name":"halfgirlfriend","author":"chetan","price":300,"av_copies":300,"sold":200}
"rainrising":{"book_name":"rainrising","author":"nirupama","price":350,"av_copies":0,"sold":320}
}

#nirupama,chetan,paule
#find book
#bookname,nocopies
#alchemist



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