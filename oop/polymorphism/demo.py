### polymorphism ...many forms
##method overloading...same method name and different number of arguments
##method overriding...same method name and same number of arguments



###method overloading example
# class Operators:
#     def num(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#         print(self.n1+self.n2)
#
# class Display(Operators):
#     def num(self,n3):
#         self.n3=n3
#         print(self.n3)
# d=Display()
# d.num(3)
#
# class Operators:
#     def num(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#         print(self.n1+self.n2)
#
# class Display(Operators):
#     def num(self,n3):
#         self.n3=n3
#         print(self.n3)
# d=Display()
# d.num(3,4)     ## donot support
#

###method overriding example
class Person:
    def printval(self,name):
        self.name=name
        print("inside person method",self.name)
class Child(Person):
    def printval(self,class1):
        self.class1=class1
        print("inside child method",self.class1)
ch=Child()
ch.printval("abc")

