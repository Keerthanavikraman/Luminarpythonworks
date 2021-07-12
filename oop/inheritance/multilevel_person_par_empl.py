class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Parent(Person):
    def tvalue(self,address,job):
        self.address=address
        self.job=job
        print(self.address,self.job)
class Employee(Parent):
    def evalue(self,id,company):
        self.id=id
        self.company=company
        print(self.id,self.company)
pa=Parent()
pa.tvalue("abc","software engineer")
pa.pvalue("anu",25)

em=Employee()
em.evalue(2503,"white rabbit")
em.tvalue("abc","software engineer")
em.pvalue("minnu",22)