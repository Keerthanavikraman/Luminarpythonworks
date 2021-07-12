def factorial(x):
    if x==1:
        return 1
    else:
        return(x * factorial(x-1))        #factorial(x-1)-->function call
num=int(input("enter the number"))
print("the factorial of",num,"is",factorial(num))