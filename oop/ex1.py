#create a child class that will inherit all of the variables and methods of vehicle class



class Vehicle:
    def vdetails(self, model, mileage, max_speed):
        self.model = model
        self.mileage = mileage
        self.max_speed = max_speed
        print(self.model, self.mileage, self.max_speed)
class Car(Vehicle):
    def cdetails(self,color,regno):
        self.color = color
        self.regno = regno
        print(self.color, self.regno)



car1 = Car()
car1.vdetails("jeep", 20, 100)
car1.cdetails("black","KL25J6201")

car2=Car()
car2.vdetails("range rover",30,150)
car2.cdetails("white","KL25K3838")
