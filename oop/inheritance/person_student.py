# inheritance


#  single inheritance


# class Person:
#     def pdetails(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.address=address
#         print(self.name,self.age,self.address)
# class Student:
#     def sdetails(self,roll_no,department,mark):
#         self.roll_no=roll_no
#         self.department=department
#         self.mark=mark
#         print(self.roll_no,self.department,self.mark)
#
# pe=Person()
# pe.pdetails("anu",24,"abc")
# st=Student()
# st.sdetails(1,"cs",89)



class Person:
    def pdetails(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        print(self.name, self.age, self.address)


class Student(Person):
    def sdetails(self, roll_no, department, mark):
        self.roll_no = roll_no
        self.department = department
        self.mark = mark
        print(self.roll_no, self.department, self.mark)
        print(self.name,"mark is",self.mark)


# pe=Person()
# pe.pdetails("anu",24,"abc")
st = Student()
st.pdetails("anu", 24, "abc")
st.sdetails(1, "cs", 89)
