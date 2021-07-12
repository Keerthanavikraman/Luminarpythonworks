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


    def __str__(self):
        return self.name

f=open("student",'r')
for line in f:
    #print(line)
    data=line.rstrip("\n").split(",")
    #print(data)
    ##print(data)
    name=data[0]
    rollno=data[1]
    course=data[2]
    mark=data[3]
    obj=Student(name,rollno,course,mark)
    print(obj)
    obj.printval()