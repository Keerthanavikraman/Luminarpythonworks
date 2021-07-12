#### oop....object oriented programming
#each program is done in objects and it consists of some concepts i.e., class,object and refernce

# class: design pattern / blue print
# object: real world entity
#reference: to perform operations on object


# class Person:  #use capital
#     def walk(self):  #method1        #self is a instance keyword
#         print("person is walking")
#     def read(self):  #method2
#         print("person is reading")
#
# obj1=Person()   #obj1 is the reference of person
# obj1.walk()
# obj1.read()
#
# obj2=Person()
# obj2.walk()
# obj2.read()

# class Person:
#     def setval(self,name,age):
#         self.name=name #instance varibale
#         self.age=age
#     def printval(self):
#         print("name::",self.name)
#         print("age::", self.age)
# pe=Person()
# pe.setval("anu",24)
# pe.printval()

class Person:
    def setval(self,name,age):
        self.name=name #instance varibale
        self.age=age
    def printval(self):
        print("name::",self.name)
        print("age::", self.age)
pe=Person()
name=input("enter the name")
pe.setval("name",24)
pe.printval()


