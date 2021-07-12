s1=[1,3,4,567,89,2,6,7,89]
s2=[1,2,3,4,5]
se=[]
for i in s1:
     if i in s2:
         se.append(i)
print(se)