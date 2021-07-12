#largest number
lst=[1,2,3,4,5,6,7]
from functools import reduce
largest=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(largest)
