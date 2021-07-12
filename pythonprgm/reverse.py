no=int(input("enter "))
rev=0
while(no!=0):
    digit=no%10 #reminder
    rev=rev*10+digit
    no=no//10
print(rev)


# type conversion
# a=123
# print(float(a))

