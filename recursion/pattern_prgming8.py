   #        *
   #      *   *
   #    *   *    *
   # *    *    *     *

def triangle(n):
    k = n
    #print(n)
    for i in range(0, n):
        for r in range(0,k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1): #0,1,2
            print("*",end="")
        print("\r")
triangle(5)


# n=int(input("enter the no. of rows"))
# for i in range(1,n):
#     print(" " * (n-i),end=" ")
#     for j in range(0,i):
#         print("*",end="")
#     print()