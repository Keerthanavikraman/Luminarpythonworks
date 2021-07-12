#multilevel/hierarchial inheritance

class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):
    def cvalue(self,address,cls):
        self.address=address
        self.cls=cls
        print(self.address,self.cls)
class Student(Child):
    def svalue(self,roll_no,mark):
        self.roll_no=roll_no
        self.mark=mark
        print(self.roll_no,self.mark)
ch=Child()
ch.cvalue("abc",9)
ch.pvalue("anu",25)

st=Student()
st.svalue(2,98)
st.cvalue("abc",9)
st.pvalue("minnu",22)