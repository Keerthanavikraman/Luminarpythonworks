
import re
rule="[L][U][M]\d{2}[P][Y]\d{3}"

f=open("reg_no",'r')
f1=open("reg_no1","w")

for num in f:
    number=num.rstrip("\n")
    matcher= re.fullmatch(rule,number)
    if matcher!=None:
        f1.write(num)
       #f1.write(number)
       #f1.write('\n')




import re
rule="[L][U][M]\d{2}[P][Y]\d{3}"
#rule="[L][U][M]\d{2}[B][D]\d{3}"
f=open("reg_no",'r')
f1=open("reg_no1","w")
#f2=open("reg_no3","w")
for num in f:
    number=num.rstrip("\n")
    matcher= re.fullmatch(rule,number)
    if matcher!=None:
        f1.write(num)
       #f1.write(number)
       #f1.write('\n')
# for num in f:
#     number=num.rstrip("\n")
#     matcher= re.fullmatch(rule,number)
#     if matcher!=None:
#         f2.write(num)