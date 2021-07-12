import re
n= input("enter the email to validate")
#x='[a-zA-Z0-9]+[@][a-z]+[.][a-z]+'
#x='[a-zA-Z0-9]+[@][gmail]+[.][a-z]+'
#x='[a-zA-Z0-9]+[@][gmail]+[.][com]+'
x='[a-zA-Z0-9]+[@][a-z]+[.][a-z]{2,3}$'
match = re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")

