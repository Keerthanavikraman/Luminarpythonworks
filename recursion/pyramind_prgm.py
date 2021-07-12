#        *          i=0
#      *   *        i=1
#    *   *    *     i=2
# *    *    *     * i=3




num = int ( input( " enter the number of rows " ) )  #num=4
for i in range( 0 , num ):                      #(0,4)-->(0,1,2,3)                 #i=0                      #i=1
    for j in range( 0 , num - i - 1 ):              # first for loop for space  #(0,4-0-1)=(0,3)           #(0,4-1-1)=(0,2)
        print( end =   "  " )                       #this statement will print thrice,so it have 3space    # 2 spaces
    for j in range( 0 , i + 1 ):                  #second for loop to print *
                                            #i=0 (0,0+1)=(0,1)       #i=1 (0,1+1)=(0,2)
        print(" * ", end = " ")                  # single star        #2 stars
    print( )



