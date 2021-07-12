#what is method overriding give an example using Teacher class


#same method name and same number of arguments are called method overriding


class Teacher:
    def printval(self,name):
        self.name=name
        print("inside person method",self.name)
class Child(Teacher):
    def printval(self,class1):
        self.class1=class1
        print("inside child method",self.class1)
ch=Child()
ch.printval("abc")
