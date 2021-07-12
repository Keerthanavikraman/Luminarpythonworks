x=input("enter a string")
count=0
for i in x:
    count=x.count(i)
    if count>1:
        break
print("fisrt recursive element is",i)