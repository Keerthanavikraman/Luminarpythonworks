class Employee:
    company_name="white rabit"
    def setval(self,name,empl_id,salary,department):
        self.name=name
        self.empl_id=empl_id
        self.salary=salary
        self.department=department
    def printval(self):
        print(self.name,self.empl_id,self.salary,self.department,Employee.company_name)
emp=Employee()
emp.setval("keerthana",2503,20000,"software")
emp.printval()

emp2=Employee()
emp2.setval("manu",2303,25000,"software")
emp2.printval()
