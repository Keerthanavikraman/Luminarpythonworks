list=[1,2,3,4,5,6,7,8,9,23,44,56]
prime=[]
nonprime=[]
for i in list:
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
               nonprime.append(i)
               break
        else:
            prime.append(i)

print("prime list",prime)
print("nonprime list",nonprime)

