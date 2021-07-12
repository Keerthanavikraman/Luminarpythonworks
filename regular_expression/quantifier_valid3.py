#starting with a ending with b
#ab agfjhfhgjhb a65786:"":b aaabbb aFDDGdgfb

import re
n= input("enter ")
x='^a\w*\W*b$'
#x="(^a[a-zA-Z0-9\W]*b$)"
match = re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")




#PEC16CS024

import re
n= input("enter ")

x="([a-zA-Z]{3}[0-9]{2}[A-Z]{2}[0-9]{3})"
match = re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")

