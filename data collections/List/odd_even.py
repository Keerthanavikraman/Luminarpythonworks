list1=[1,2,3,4,5,6,7,8,9,98,78,65,43,56,23,14,63,78]
odd=[]
even=[]
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("even lst",even)
print("odd lst",odd)
