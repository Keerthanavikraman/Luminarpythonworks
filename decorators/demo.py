#adding extra features without changing function definition
#wrapper...means inner function


def check(func):          #impppp
    def wrapper(name,age):  #("anu",10)
        if age<18:
            print("not eligible")
        else:
            return func(name,age)   #vaccine("anu",10)
    return wrapper


@check
def vaccine(name, age):
    print(name, "eligible for vaccination")
vaccine("anu", 19)

@check
def eligible_check(name,age):    #no of variables/arguments should be same
    print(name)
eligible_check("amal",14)