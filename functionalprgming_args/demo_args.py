# def add(num):
#     print(num1+num2)
# add(2,6,8)    #3 arguments are taken

#arguments(actual values)
#parameters(variables passed)
def add(*args):
    #print(args)
    sum=0
    for i in args:
        sum=i
    print(sum)
add(2,3,4,5,6)


# args=(1,2,3,4,5)
# sum=0
# for i in args:
#     sum=i
# print(sum)