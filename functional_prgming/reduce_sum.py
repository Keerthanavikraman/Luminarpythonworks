#to iterate a single value

#map-object
#bultins -map,filter,print,max,min,sort,sum
#functools -reduce

lst=[1,2,3,4,5,6,7]
from functools import reduce
total=reduce(lambda num1,num2:num1+num2,lst)
print(total)



