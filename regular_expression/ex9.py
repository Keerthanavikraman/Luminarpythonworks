#write a code to validate string starting and ending with a uppercase_letter except special characters minimum length 5 -maximum length 10


import re
n= input("enter ")

x='^[A-Z][a-zA-Z0-9]{3,8}[A-Z]$'
match = re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")


#AsfdhjkhjjfA