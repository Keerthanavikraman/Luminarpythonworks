# for i in range(1001):
#     num=i
#     result=0
#     n=len(str(i))
#     while(i!=0):
#         digit=i%10
#         result=result+digit**n
#         i=i//10
#     if num==result:
#         print(num)

num=int(input("enter a number"))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if num==sum:
    print("armstrong number",num)
else:
    print("not armstrong number",num)
