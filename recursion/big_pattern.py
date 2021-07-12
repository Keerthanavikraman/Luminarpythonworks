# a=int(input("enter the initial range"))
#
# b=int(input("enter the final range"))
#
# for i in range(0,b):
#     for j in range(0,i+1):
#         print("1", end="")
#     print("")
# for i in range(b+1,0,-1):
#     for j in range(0,i-1):
#         print("2", end="")
#     print("")
# for i in range(0,b):
#     for j in range(0,i+1):
#         print("3", end="")
#     print("")
# for i in range(b+1,0,-1):
#     for j in range(0,i-1):
#         print("4", end="")
#     print("")
#



a=int(input("enter the initial range"))
b=int(input("enter the final range"))
r=5
for i in range(a,b):
    if (i%2==0):
        #print(i)
        for k in range(r,0,-1):
            for j in range(0,k):
                print(i,end="")
            print("\r")
    else:
        for l in range(r):
            for m in range(0,l+1):
                print(i,end="")
            print("\r")






