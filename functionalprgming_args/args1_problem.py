#print name of employee whose eid=1002



employees={
    1000:{"eid":1000,"ename":"ajay","salary":34000,"designation":"developer"},
    1001:{"eid":1001,"ename":"arun","salary":30000,"designation":"developer"},
    1002:{"eid":1002,"ename":"akhil","salary":21000,"designation":"hr"},
    1003:{"eid":1003,"ename":"anu","salary":45000,"designation":"Analyst"},
}
#print(employees[1002]["ename"])
#print(employees[1002])


#print using user input


# eid=int(input("enter the id"))
# prop=input("enter property option eid,ename,salary,designation")
# if eid in employees:
#     print(employees[eid][prop])
# else:
#     print("invalid eid")



eid=int(input("enter the id"))
prop=input("enter property option eid,ename,salary,designation")
if eid in employees and prop in employees[eid]:    #and checks both conditions
    print(employees[eid][prop])

else:
    print("invalid eid or property")