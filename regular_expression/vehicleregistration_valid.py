#KL25JK6201


import re
n= input("enter the number to validate")

x='[K][L]\d{2}[A-Z]{2}\d{4}$'
#x='[K][L]\d{2}[A-Z]{2}\d{4}'

#x='[A-Z]{2}\d{2}[A-Z]{2}\d{4}$'
match = re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")