# # constructor  : to initialise instance variable
# # constructor automatically invoke when creating object

class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def printval(self):
        print(self.name,self.age,self.address)
pe=Person("anu",24,"abc")
pe.printval()

class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def printval(self):
        print(self.name,self.age,self.address)
name=input ("enter the name")
pe=Person(name,24,"abc")
pe.printval()

pe1=Person("minnu",22,"cde")
pe1.printval()