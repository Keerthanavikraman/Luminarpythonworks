class Parent:
    def setval(self,name,address,phone_nbr):
        self.name=name
        self.address=address
        self.phone_nbr=phone_nbr
    def printval(self):
        print(self.name,self.address,self.phone_nbr)

parent1=Parent()
parent1.setval("shyni","kavyakeerthanam",1234)
parent1.printval()

parent2=Parent()
parent2.setval("sindu","keerthanam",5678)
parent2.printval()