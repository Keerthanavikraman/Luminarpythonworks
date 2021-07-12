#without changing function definitiom ...decorators


def revert(func):    #decorator functn always accept a functiom      #sub(1,10)
    def wrapper(num1,num2):   #inner function accept the sub function  #(1,10)
        if (num1<num2):    #(1<10)
            (num1,num2)=(num2,num1)    #(10,1)
            return func(num1,num2) #sub(10,1)
        else:
            return func(num1,num2)
    return wrapper

@revert
def sub(num1,num2):
    return num1-num2
print(sub(1,10))



# def revert(func):
#     def wrapper(num1,num2):
#         if (num1<num2):
#             (num1,num2)=(num2,num1)
#             return func(num1,num2) #sub(5,10)
#     return wrapper
#
# @revert
# def sub(num1,num2):
#     return num1-num2
# print(sub(5,10))

# def revert(func):
#     def wrapper(num1,num2):
#         if (num1<num2):
#            return func(num2,num1) #sub(5,10)
#     return wrapper
#
# @revert
# def sub(num1,num2):
#     return num1-num2
# print(sub(5,10))