#when is the finally block executed.explain with example
#finally block is always executed after leaving the try statement .In case if some exception was not handled by except block,
#it is re-raised after execution of finally block.


a=[1,3,2,4]
b=int(input("enter index"))
try:
    print(a[b])
except Exception as e:
    print("exception occured", e)
finally:
    print("inside finally")
