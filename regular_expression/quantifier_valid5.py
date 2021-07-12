#starting with a upper case letter
#numbers,lowercase,symbols
#Abv5<  G6   R. Tt Dhgfhjkhg6t667":';;



import re
n= input("enter ")

x="(^[A-Z]{1}[a-z0-9\W]+)"
match = re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")








