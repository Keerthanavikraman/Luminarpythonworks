class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Parent:
    def tvalue(self,address,job):
        self.address=address
        self.job=job
        print(self.address,self.job)
class Employee(Person,Parent):
    def evalue(self,id,company):
        self.id=id
        self.company=company
        print(self.id,self.company)
em=Employee()
em.pvalue("Keerthana Vikraman",22)
em.tvalue("Kavyakeerthanam house","Business")
em.evalue(2503,"White Rabit")