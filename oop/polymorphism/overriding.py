class Employee:
    def printval(self,company):
        self.company=company
        print("inside employee method",self.company)
class Parent(Employee):
    def printval(self,job):
        self.job=job
        print("inside parent method",self.job)
pa=Parent()
pa.printval("software engineer")