# *
# * *
# * * *
# * * * * *

n=int(input("enter the number of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()


# n=int(input("enter the number of rows"))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end="")
#     print()

# def pattern(n):
#     for i in range(0,n):
#         for j in range(0,i+1):
#             print("*",end="")   #end is a keyword for giving space
#         print()                 #newline
#
# pattern(5)

#print("/r")  #next row

