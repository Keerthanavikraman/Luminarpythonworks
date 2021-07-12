class Child:
    def setval(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    def printval(self):
        print(self.name,self.age,self.weight)
child1=Child()
child1.setval("minnu",10,15)
child1.printval()

child2=Child()
child2.setval("nannu",15,20)
child2.printval()






