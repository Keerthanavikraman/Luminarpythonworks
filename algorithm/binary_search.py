#linear search

#lst=[4,3,2,5,6,7,8,9,9,99,1,3,55,77,88,55,44,22]
#each element is checked for the searched element present or not,
# if the searched element is present at the lat a number of iterations want to be performed
#for this binary search is used
#in this the lengthy list is sorted and a middle element is set and divided into 2 list

#searched elemet is greater or lesser than middle element

# a=[1,4,2,3,5]
# a=[1,2,3,4,5] # sorted #middle element=3   # 3 is greater than searched element
# b=5 # searched element

# a=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# middle element=10
# search element =14
# again
# a=[11,12,13,14,15]
# middle element=13
# the searched element (14) is greater than the middle element


#####  program #######

lst=[1,6,5,8,7,9,10,11,12,13,14,15,16,17,18,19]

def bsearch():
    lst.sort()
    print(lst)
    ele = int(input("enter the element"))
    fla = 0
    low = 0
    upp = len(lst)-1
    #print upper
    while low <= upp:
        mid = (low+upp) // 2
        #print(mid)
        if ele > lst(mid):
            low = mid + 1
        elif ele < lst(mid):
            upp = mid - 1
        elif ele == lst(mid):
            print(mid)
            fla = 1
            break
    if fla == 1:
        print("found")
    else:
        print("not found")

bsearch()