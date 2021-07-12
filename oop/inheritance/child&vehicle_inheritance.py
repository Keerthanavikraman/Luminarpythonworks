#create a child class bus that will inherit all of the variables and methods of vehicle class


class Childbus:
    def cvalue(self,busno,bustime,school):
        self.busno=busno
        self.bustime=bustime
        self.school=school
        print(self.busno,self.bustime,self.school)

class Vehicle(Childbus):
    def vehvalue(self,model,reg_no,color):
        self.model=model
        self.reg_no=reg_no
        self.color=color
        print(self.model,self.reg_no,self.color)

ve=Vehicle()
ve.vehvalue("schoolbus",1234,"yellow")
ve.cvalue(12,"6AM","lotus public school")