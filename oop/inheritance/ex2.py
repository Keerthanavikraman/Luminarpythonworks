#create an example for 3 types of inheritance in one program by using college as main class



class College:
    def cdetails(self, collegename, address):
        self.collegename = collegename
        self.address = address
        print(self.collegename, self.address)


class Student(College):
    def sdetails(self, roll_no, department, mark):
        self.roll_no = roll_no
        self.department = department
        self.mark = mark
        print(self.roll_no, self.department, self.mark)

class Teacher(Student,College):
    def tdetails(self,name,id,subject):
        self.name=name
        self.id=id
        self.subject=subject
        print(self.name,self.id,self.subject)
clg=College()                  #single
clg.cdetails("PEC", "college of engineering pathanapuram")
st = Student()
st.sdetails(24, "cs", 89)
teach=Teacher()
teach.tdetails("shyni",2563,"maths")


t1=Teacher()                 #multiple
t1.cdetails("snit","sreenaraya institute")
t1.sdetails(12,"civil",90)
t1.tdetails("sethu","1493","python")

st1=Student()                #multilevel
st1.cdetails("ihrd","clg eng adoor")


tch1=Teacher()
tch1.tdetails("kavya",1234,"c")
tch1.sdetails(34,"cs",56)