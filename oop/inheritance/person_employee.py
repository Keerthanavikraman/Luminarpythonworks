#single inheritance


class Person:      #parent class/base class /super class
    def pdetails(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        print(self.name, self.age, self.address)


class Employee(Person):       #child class/derived class/sub class
    def edetails(self, id,department,company):
        self.id = id
        self.department = department
        self.company = company
        print(self.id, self.department, self.company)
        print(self.name,"department is",self.department)

em = Employee()
em.pdetails("minnu", 22, "kavyakeerthanam")
em.edetails(2503, "software", "white rabit")
