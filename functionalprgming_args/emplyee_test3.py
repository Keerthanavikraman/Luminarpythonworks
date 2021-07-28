
#employees={1000:{"id":1000,"name":"ajay","design":"developer","exp":2,"salary":25000}}

f1=open("employee_test3qstn","r")
employees={}
for line in f1:
    #print(line)
    eid,name,design,exp,salary=line.rstrip("\n").split(",")
    employees[int(eid)]={"eid":eid,"name":name,"design":design,"exp":exp,"salary":salary}
print(employees)

def printEmployee(id=None,**kwargs):
    if id in employees:
        print(employees[id]["name"])
        if "prope" in kwargs:
            if kwargs["prope"] in employees[id]:
                print(employees[id][kwargs["prope"]])
            else:
                print("invalid property")
    else:
        print("invalid id")
        #raise Exception("invalid id")




# try:
#     id=int(input("enter id"))
#     printEmployee(id)
#     prop=input("enter a property")
#     printEmployee(id,prope=prop)
# except Exception as e:
#     print("Exception occured- invalid id",e)
#     print("please check the id you entered")
#
# except:
#     print("Exception occured- invalid property")
#     print("please enter a valid property")


printEmployee(id=1000,prop="salary")