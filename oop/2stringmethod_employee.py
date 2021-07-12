class Employee:
    company_name = "white rabit"

    def __init__(self,name,id,salary,empl_exp):
        self.name=name
        self.empl_exp=empl_exp
        self.id=id
        self.salary=salary

    def printDetails(self):
        print("name of the company", Employee.company_name)
        print("name of employee",self.name)
        print("id of employee",self.id)
        print("salary of employee",self.salary)
        print("experience of employee",self.empl_exp)
    def __str__(self):
        return str(self.empl_exp)+self.name
em1=Employee("Keerthana",2503,25000,2)
print(em1)
em2=Employee("Vinayak",2802,30000,3)
print(em2)

