class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):
    def cvalue(self,school,cls):
        self.school=school
        self.cls=cls
        print(self.school,self.cls)
class Parent(Person):
    def tvalue(self,address,job):
        self.address=address
        self.job=job
        print(self.address,self.job)
class Student(Child):
    def svalue(self,roll_no,mark):
        self.roll_no=roll_no
        self.mark=mark
        print(self.roll_no,self.mark)

ch=Child()
ch.cvalue("lotus public school",9)
ch.pvalue("keerthana",22)

pa=Parent()
pa.pvalue("keerthana",22)
pa.tvalue("kavyakeerthanam","software engineer")



st=Student()
st.svalue(2,98)
st.cvalue("lotus public school",9)
st.pvalue("keerthana",22)