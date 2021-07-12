set1={1,2,3,4,5,6,7,8,9,98,78,65,43,56,23,14,63,78}
odd=set()
even=set()
for i in set1:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)

print("even set",even)
print("odd set",odd)
