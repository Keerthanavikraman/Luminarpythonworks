class Addition:
    def setval(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def printval(self):
        print(self.n1+self.n2)
# add1=Addition()
# add1.setval(10,100)
# add1.printval()

#
add1=Addition()
no1=int(input("enter no1"))
no2=int(input("enter no2"))
add1.setval(no1,no2)
add1.printval()
