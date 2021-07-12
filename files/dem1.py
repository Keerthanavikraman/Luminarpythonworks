f1=open("dem","r")
count={}
for i in f1:
    #print(i)
    words=i.rstrip('\n').split(" ")
    print(words)
    for word in words:
        if word not in count:
            count.update({word:1})
        else:
            val=int(count[word])
            val+=1
            count.update({word:val})
print(count)


count={}
data="hello hai hello"
words=data.split(" ")
for i in words:
    if i not in count:
        count.update({i:1})
    else:
        val=int(count[i])
        val+=1
        count.update({i:val})
print(count)

