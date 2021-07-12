# a=[1,2,3,4,5,5,6,7,8,9]
# b=[]
# for i in a:
#     b.append(i*5)
# print(b)

# a=[1,2,3,4,5,5,6,7,8,9]
# b=[i*5 for i in a]     #this can be apply in only list called list comprehension
# print(b)

a=[i for i in range(1,100) if i%5==0]
print(a)
print(len(a))

