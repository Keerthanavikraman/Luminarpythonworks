n=int(input("enter how many numbers you want in the series "))
first=0
second=1
for i in range(n):
    print(first)
    temp=first
    first=second
    second=temp+second
#
# nterms=10
#first two terms
# n1=0
# n2=1
# count=0
# print("fibonacci series:")
# while count<nterms:
#     print(n1)
#     nth=n1+n2
# update values
#     n1=n2
#     n2=nth
#     count+=1


n1=0
n2=1
for i in range(10):
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth





