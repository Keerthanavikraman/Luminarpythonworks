a=int(input("enter num"))
if a>0:
    fact=1
    for i in range(1,a+1):
        fact= fact * i
    print(fact)
elif a==0:
    print("fact of 0 is 1")
else:
    print("please enter a positive number")