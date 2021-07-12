# x=2
# def printval():
#     x=10
#     print(x)
# printval()
# print(x)



# def printval():
#     global x
#     x=10
#     print(x)
# printval()
# print(x)

# def printval():
#     global x,a
#     a=8
#     x=10
#     print(x)
# printval()
# print(x)
# print(a)

# def printval():
#     global x,a
#     a=8
#     x=10
#     x=x+1
#     print(x)
# printval()
# print(x)
# print(a)


def printval():
    global x,a
    a=8
    x=10
    x=x+1
    a=a-1
    print(x)
printval()
print(x)
print(a)
