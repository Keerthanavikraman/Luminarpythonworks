#create objects of the following file and print details of student with maximum mark?

class Student:
    def __init__(self, name,rollno,course,mark):
        self.name = name
        self.rollno= rollno
        self.course=course
        self.mark=mark
    def printval(self):
        print("name:",self.name)
        print("age:",self.rollno)
        print("course:",self.course)
        print("mark:",self.mark)

lst=[]
f=open("ex6","r")
for i in f:
    data=i.rstrip("\n").split(",")
    #print(data)
    name=data[0]
    rollno=data[1]
    course=data[2]
    mark=data[3]
    s1=Student(name,rollno,course,mark)
    #s1.printval()
    lst.append(s1)
#print(lst)
mark=[]
for st in lst:
    mark.append(st.mark)
print(mark)
for st in lst:
    if(st.mark==max(mark)):
        print(st.rollno,st.name,st.course,st.mark)
        print(st.mark)    #maximum mark