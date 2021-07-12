# my_list=[111,-15,-26,15,1,0,8,876,100,54,23,-64,2]
# print(my_list)
# my_list.sort()
# print(my_list)


# list=[2,5,-3,9,8,-6,9,-6,3,112,34,]
# list.sort()
# print(list)

#####   important#######
# my_list=[111,-15,-26,2,5,-3,9,8,-6,9,-6,3,112,34,]
# new_list=[]
# while my_list: #iterate
#     min=my_list[0]   #min=111
#     for x in my_list:  #111
#         if x in my_list:
#             if x<min:     #111<111
#                 min=x
#     new_list.append(min)
#     my_list.remove(min)
# print(new_list)


my_list=[2,5,-3,9,8,-6,9,-6,3,112,34,]
for i in range(0,len(my_list)):
    for j in range(i+1,len(my_list)):
        if(my_list[i]>my_list[j]):
            my_list[i],my_list[j]=my_list[j],my_list[i]
print(my_list)

