class Animal:
    def __init__(self,typee,color,legs,speed):
        self.typee=typee
        self.color=color
        self.legs=legs
        self.speed=speed
    def printval(self):
        print(self.typee,self.color,self.legs,self.speed)


class Child(Animal):
    def __init__(self,petage,petname,typee,color,legs,speed):
        super().__init__(typee,color,legs,speed)
        self.petage=petage
        self.petname=petname

    def print(self):
        print(self.petage)
        print(self.petname)

ch=Child(2,"hibru","dog","white",4,24)
ch.printval()
ch.print()

ch1=Child(4,"bella","dog","white",4,26)
ch1.printval()
ch1.print()