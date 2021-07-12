# class Employee:
#     def setval(self,name,empl_id,salary,department,company_name):
#         self.name=name #instance varibale
#         self.empl_id=empl_id
#         self.salary=salary
#         self.department=department
#         self.company_name=company_name
#     def printval(self):
#         print("name::",self.name)
#         print("empl_id::", self.empl_id)
#         print("salary::",self.salary)
#         print("department::",self.department)
#         print("company_name::",self.company_name)
# pe=Employee()
# pe.setval("keerthana",2503,20000,"software","white_rabit")
# pe.printval()

class Employee:
    def setval(self,name,empl_id,salary,department,company_name):
        self.name=name #instance varibale
        self.empl_id=empl_id
        self.salary=salary
        self.department=department
        self.company_name=company_name
    def printval(self):
        print(self.name,self.empl_id,self.salary,self.department,self.company_name)
emp=Employee()
emp.setval("keerthana",2503,20000,"software","white_rabit")
emp.printval()

emp2=Employee()
emp2.setval("manu",2303,25000,"software","luminar")
emp2.printval()



# class Employee:
#     def setval(self,name,empl_id,salary,department,company_name):
#         self.name=name #instance varibale
#         self.empl_id=empl_id
#         self.salary=salary
#         self.department=department
#         self.company_name=company_name
#     def printval(self):
#         print("name::",self.name)
#         print("empl_id::", self.empl_id)
#         print("salary::",self.salary)
#         print("department::",self.department)
#         print("company_name::",self.company_name)
# pe=Employee()
# name=input("enter the name")
# employ_id=int(input("enter the emplo_id"))
# salary=int(input("enter the salary"))
# department=input("enter the department")
# company_name=input("enter the company_name")
# pe.setval("name","employ_id","salary","department","company_name")
# pe.printval()