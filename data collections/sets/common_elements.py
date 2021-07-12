# s1={1,3,4,567,89,2,6,7,89}
# s2={1,2,3,4,5}
# k= (set(s1)&set(s2))
# for i in k:
#      print(i)

s1={1,3,4,567,89,2,6,7,89}
s2={1,2,3,4,5}
for i in s1:
     if i in s2:
         print(i)

s1={1,3,4,567,89,2,6,7,89}
s2={1,2,3,4,5}
se=set()
for i in s1:
     if i in s2:
         se.add(i)
print(se)