#a = "abc"
# b="bcd"
# k= (set(a)&set(b))
# for i in k:
#     print(i)

# a = "abc"
# b = "bcd"
# for i in a:
#     if i in b:
#         print(i)

a="abc"
b="yy"
c=""
for i in a:
    if i in b:
        c=c+1
if c=="":
    print("no common")
else:
    print(c)

