import re
rule='[K][L]\d{2}[A-Z]{2}\d{4}$'
f=open("vehicle",'r')
f1=open("validregnum","w")
for num in f:
    number=num.rstrip("\n")
    matcher= re.fullmatch(rule,number)
    if matcher!=None:
        f1.write(num)
