pattern=input("enter")
count={}
for i in pattern:
    if i not in count:
        count.update({i:1})
    else:
        print(" first recursive element",i)
        break