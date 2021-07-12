# person={"name":"ram","age":24}
#
# if ("gender" in person):
# #print ("gender" in person):


# def add(*args):
#     print(args)
# add(10, 20, 30)
#
#
# def add(**args):
#     print(args)
# add(num1=10, num2=20, num3=30)
#
# def add(**kwargs):
#     print(kwargs)
# add(num1=10, num2=20, num3=30)


def add(*args,**kwargs):
    print(args)
    print(kwargs)
add(10, 20, 30,num1=10, num2=20, num3=30)