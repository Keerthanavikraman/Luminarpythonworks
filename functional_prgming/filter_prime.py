lst=[12,13,14,15,17,]

def prime(num):
    flg=0
    for i in range(2,num):
        if num%i==0:
            flg+=1
            break
    if flg==0:
        return True
res=list(filter(prime,lst))
print(res)

