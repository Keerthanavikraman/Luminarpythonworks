#create a Person class using constructor and build a child class for employee


class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def printval(self):
        print(self.name,self.age,self.address)
class Employee:
    def setval(self,name,empl_id,salary,department,company_name):
        self.name=name
        self.empl_id=empl_id
        self.salary=salary
        self.department=department
        self.company_name=company_name
    def printval(self):
        print(self.name,self.empl_id,self.salary,self.department,self.company_name)

pe1=Person("minnu",22,"cde")
pe1.printval()

emp=Employee()
emp.setval("keerthana",2503,20000,"software","white_rabit")
emp.printval()