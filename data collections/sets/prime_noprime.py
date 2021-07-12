sett={1,2,3,4,5,6,7,8,9,23,44,56}
prime=set()
nonprime=set()
for i in sett:
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
               nonprime.add(i)
               break
        else:
            prime.add(i)

print("prime set",prime)
print("nonprime set",nonprime)


