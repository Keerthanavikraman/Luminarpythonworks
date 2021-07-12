class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name",self.name)
        print("age",self.age)
class Employee(Person):   #inheriting person class inside employee class
    def __init__(self,id,company,name,age):
        super().__init__(name,age)
        self.id=id                   #setting attributes
        self.company=company
    def print(self):
        print(self.id)
        print(self.company)
em=Employee(2503,"White Rabit","Keerthana Vikraman",22)
em.printval()
em.print()