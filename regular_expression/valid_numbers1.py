import re
f1=open("valid_numbers",'r')
x='[+][9][1]\d{10}'
for num in f1:
    number=num.rstrip("\n")
    matcher= re.fullmatch(x,number)
    if matcher!=None:
        print(num)













