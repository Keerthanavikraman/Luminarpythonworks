#write a python program that matches a string that has an 'a' followed by numbers ending in 'b'




import re
n= input("enter")
x="(^a[0-9]+b$)"
match = re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")







