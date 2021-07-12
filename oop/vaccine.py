class Vaccine:
    def setval(self,age,name,gender):
        self.age=age
        self.name=name
        self.gender=gender

    def printval(self):
        print(self.age>=18,self.name,self.gender)

vacc1=Vaccine()
vacc1.setval(30,"minnu","female")
vacc1.printval()

vacc2=Vaccine()
vacc2.setval(12,"hibru","male")
vacc2.printval()
