def revert(func):
    def wrapper(num1,num2):
        if (num1<num2):
            (num1,num2)=(num2,num1)
            return func(num1,num2) #div(5,10)
        #else:
            #return func(num1,num2)
    return wrapper

@revert
def div(num1,num2):
    return num1/num2
print(div(5,10))     #(5,10)



def revert(func):
    def wrapper(num1,num2):
        if (num1<num2):
            (num1,num2)=(num2,num1)
            return func(num1,num2) #div(5,10)
        else:
            return func(num1,num2)
    return wrapper

@revert
def div(num1,num2):
    return num1/num2
print(div(10,5))      #(10,5)


def zeronotrequired(func):
    def wrapper(num1,num2):
        if num1==0 | num2==0:
            raise Exception("invalid parameter")
        else:
            return func(num1,num2)
    return wrapper
#customized exception
@zeronotrequired
def div(num1,num2):
    return num1/num2
try:
    print(div(10,0))
except Exception as e:
    print(e.args)
