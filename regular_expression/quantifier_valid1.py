# import re
# n= "helloo"
# x='\w*'
# match = re.fullmatch(x,n)     #fullmatch is same as finditer which is used in valid,invalid problems
# if match is not None:
#     print("valid")
# else:
#     print("invalid")



import re
n="56kg"
#x='[0-9]{2}[a-z]{2}'
# x='[0-9]{2}[k][g]'
# x='\d{2}[k][g]'
# x='[5][6]\w{2}'
match = re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")

