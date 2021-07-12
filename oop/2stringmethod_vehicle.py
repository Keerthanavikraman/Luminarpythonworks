##2 string method


class Vehicle:

    def vehmet(self,model,reg_no,color):
        self.model=model
        self.reg_no=reg_no
        self.color=color
        print(self.model,self.reg_no,self.color)
    def __str__(self):
        return self.model
vehicle1=Vehicle()
vehicle1.vehmet("range rover","KL256201","black")
print(vehicle1)
vehicle2=Vehicle()
vehicle2.vehmet("jeep","KL253838","black")
print(vehicle1)






