# * * * * *
# * * * *
# * * *
# * *
# *

# n=int(input("enter the number of rows"))
# for i in range(n+1,0,-1):
#     for j in range(0,i-1):
#         print("*",end="")
#     print()


# def pattern(row):
#     for i in range(row,0,-1):   #0,n
#         for j in range(0,i):    #0,n-i
#             print("*",end="")
#         print()
# pattern(5)


def pattern(n):
    for i in range(0,n):   #0,n
        for j in range(0,n-i):    #0,n-i
            print("*",end="")
        print()
pattern(5)
