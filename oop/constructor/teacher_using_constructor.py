class Teacher:
    college_name="college of engineering,pathanapuram"
    def __init__(self,name,sub,department,teacher_id):
        self.name=name
        self.sub=sub
        self.department=department
        self.teacher_id=teacher_id
    def printval(self): #printdet
        print(self.name)
        print(self.sub)
        print(self.department)
        print(self.teacher_id)
        print(Teacher.college_name)
name=input ("enter the name")
teacher1=Teacher(name,"python","cs",1234)
teacher1.printval()     #printdet()

teacher2=Teacher("minnu","graphics","civil",5678)
teacher2.printval()


