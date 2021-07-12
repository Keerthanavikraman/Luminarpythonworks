

# def word_count(str):
#     counts=dict()
#     words=str.split()
#
#     for word in words:
#         if word in counts:
#             counts[word]+=1
#         else:
#             counts[word]=1
#     return counts
# print(word_count("hhy hy hlo hlo hy"))

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

str=input(" >")
words=str.split(" ")
dict={}
for i in words:
    count=words.count(i)
    dict.update({i:count})
    #print(i,count)
print(dict)