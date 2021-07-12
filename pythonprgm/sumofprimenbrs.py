# min=int(input("enter the initial range"))
# max=int(input("enter the final range"))
# for a in range(min,max):
#     if a > 1:
#         for i in range(2, a):
#             if (a % i) == 0:
#                 break
#         else:
#             print(a)


min=int(input("enter the initial range"))
max=int(input("enter the final range"))
sum=0
for a in range(min,max):
    if a > 1:
        for i in range(2, a):
            if (a % i) == 0:
                break
        else:
            sum=sum+a
print(sum)

#calculation inside
#print outside
