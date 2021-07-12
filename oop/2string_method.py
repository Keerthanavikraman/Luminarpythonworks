class College:
    collegename="LT"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def printDetails(self):
        print("college name=",College.collegename)
        print("name of student",self.name)
        print("rollno",self.rollno)
    def __str__(self):
        return str(self.rollno)+self.name+College.collegename
ob=College("anu",4)
print(ob)
ob1=College("amal",8)
print(ob1)
ob2=College("ann",5)
print(ob2)
ob3=College("al",7)
print(ob3)