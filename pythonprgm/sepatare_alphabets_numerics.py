# s="keerthana123vikraman"
# for i in s:
#     print(type(i))


# cannot calculate the separate count

# s = "keerthana123vikraman"
# count=0
# for i in s:
#     count=count+1
# print(count)


a = "keerthana123vikraman"
b="1234567890"
counta=0
countb=0

for i in a:
    if i in b:
        countb=countb+1
    else:
        counta=counta+1
print(countb)
print(counta)




