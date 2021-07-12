# inverted pyramid
#    *    *    *    *      i=4
#       *    *    *        i=3
#          *    *          i=2
#             *            i=1



num = int ( input( " enter the number of rows " ) )                    #num=4
for i in range( num , 0 ,-1 ):                                         #(4,0,-1)=(4,3,2,1)
    for j in range( 0 , num - i ):                                     #i=4 (0,4-4)=(0,0) #i=3 (0,4-3)=(0,1)
        print( end =   "  " )
    for j in range( 0 , i  ):                                          #i=4 (0,4)
        print(" * ", end = " ")
    print( )




def triangle(n):
    k = n
    #print(k)
    for i in range( n,0,-1):
        for r in range(0,k):
            print(end=" ")
        k = k + 1
        for j in range(0, i ): #0,1,2
            print("*",end="")
        print("\r")
triangle(5)




