 #         *   *   *   *   *
 #       *   *   *   *   *   *
 #     *   *   *   *   *   *   *
 #   *   *   *   *   *   *   *   *
 # *   *   *   *   *   *   *   *   *


num=int(input("enter the number of rows"))
for i in range( 0 , num ):
    for j in range( 0, num - i - 1 ):
        print( end="  " )
    for j in range( 0, i + num ):
        print(" * ", end=" ")
    print()



# def trapizoid(n):
#     k = n
#     #print(k)
#     for i in range( 0,n ):
#         for r in range(0,k):
#             print(end=" ")
#         k = k - 1
#         for j in range(0, i+5 ): #0,1,2
#             print("*",end="")
#         print("\r")
# triangle(5)