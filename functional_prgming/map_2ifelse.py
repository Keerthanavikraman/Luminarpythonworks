lst=[1,2,3,4,5,6,7]
result=list(map(lambda num:num-1 if num<5 else num+1 if num>5 else num,lst))
print(result)
