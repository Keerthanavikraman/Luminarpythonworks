#print even numbers only
#filter(function,iterables)

# lst=[1,2,3,4,5,6,7]
# even=list(filter(lambda num:num%2==0,lst))
# print(even)


lst=[1,2,3,4,5,6,7]
def is_even(num):
    return num%2==0
even=list(filter(is_even,lst))
print(even)

#print odd numbers
# lst=[1,2,3,4,5,6,7]
# odd=list(filter(lambda num:num%2!=0,lst))
# print(odd)