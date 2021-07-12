a=[1,3,2,4]
b=int(input("enter index"))
try:
    print(a[b])
except Exception as e:
    print("exception occured", e)
finally:
    print("inside finally")



