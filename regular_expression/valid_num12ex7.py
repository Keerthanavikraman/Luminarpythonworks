import re
rule='[+][9][1]\d{10}'
f=open("validnum1",'r')
f1=open("validnum2","w")
for num in f:
    number=num.rstrip("\n")
    matcher= re.fullmatch(rule,number)
    if matcher!=None:
        f1.write(num)
