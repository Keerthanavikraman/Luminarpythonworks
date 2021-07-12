# a=input("enter the string")
# vowels=0
# for i in a:
#     if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
#          vowels=vowels+1
# print("no of vowels are")
# print(vowels)

# string=input("enter")
# count=0
# for i in string:
#     if i in "aeiou":
#         count=count+1
# print(count)

string=input("enter")
v="aeiou"
count=0
for i in string:
    if i in v:
        count=count+1
if count==0:
    print("no vowels")
else:
    print(count)









#v="aeiou"