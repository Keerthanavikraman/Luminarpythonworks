#Abc6
#fgRtggg7
#gfghh8
#DFGGH6

import re
n= input("enter ")
# x='[a-zA-Z]{3}[0-9]{1}'
# x='[a-zA-Z]{7}[0-9]{1}'
#x='[a-zA-Z]{5}[0-9]{1}'
# x='[a-zA-Z]{5}[0-9]{1}'
# x='\w*[0-9]{1}'

x="[a-zA-Z]+\d{1}$"
match = re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")

