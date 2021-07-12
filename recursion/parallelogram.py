# num=int(input("enter the number of rows"))
# for i in range( 0 , num ):
#     for j in range( 0, num - i  ):
#         print( end="  " )
#     for j in range( 0, num  ):
#         print(" * ", end=" ")
#     print()

num = int(input("enter the number of rows"))
for i in range(0, num):
    for j in range(0, num + i):
        print(end="  ")
    for j in range(0, num):
        print(" * ", end=" ")
    print()

# def parallel(n):
#     k = n
#     #print(k)
#     for i in range(0, n):
#         for r in range(0,k):
#             print(end=" ")
#         k = k - 1
#         for j in range(0, n ): #0,1,2
#             print("*",end="")
#         print("\r")
# parallel(5)


# def parallel(n):
#     k = n
#     #print(k)
#     for i in range(0, n):
#         for r in range(0,k):
#             print(end=" ")
#         k = k + 1
#         for j in range(0, n ): #0,1,2
#             print("*",end="")
#         print("\r")
# parallel(5)