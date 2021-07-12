import re
n= input("enter the number to validate")

x="[0-9]{10}"
#x="\d{10}"
match = re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")



