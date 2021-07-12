#lst=[2,3,4,8,10,7] o/p [1,2,3,9,11,8] if num<5 num-1 else num+1

lst=[2,3,4,8,10,7]

op=[]
for num in lst:
    if num<5:
        op.append(num-1)
    else:
        op.append(num+1)
print(op)



num=10
res="+ve" if num>0 else"-ve"
print(res)


num1=10
num2=20
res=num1 if num>num2 else num2
print(res)



result=list(map(lambda num:num-1 if num>5 else num+1,lst))
print(result)









