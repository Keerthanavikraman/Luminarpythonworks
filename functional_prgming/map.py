#square
# lst=[1,2,3,4,5,6,7]
# res=[]
# for num in lst:
#     res.append(num**2)
# print(res)
#


# lst=[1,2,3,4,5,6,7]
# #map(function,iterables)
# sq=list(map(lambda num:num**2,lst))
# print(sq)

lst=[1,2,3,4,5,6,7]
def square(num):
    return num**2
sq=list(map(square,lst))
print(sq)