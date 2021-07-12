def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def floor(x,y):
    return x//y
def expo(x,y):
    return x**y
print("select operation")
print("1.add")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.floor dividsion")
print("6.exponent")
while True:
    choice= input("enter your choice")
    if choice in ('1','2','3','4','5','6'):
        num1=float(input("enter a number"))
        num2=float(input("enter a number"))
        if choice == '1':
            print(add(num1,num2))
        elif choice == '2':
            print(sub(num1,num2))
        elif choice == '3':
            print(mul(num1, num2))
        elif choice == '4':
            print(div(num1,num2))
        elif choice == '5':
            print(floor(num1,num2))
        elif choice == '6':
            print(expo(num1,num2))
        break
    else:
        print("invalid")

# def printval(a):
#     print("hello",a")
# def printval(b,c):
#     print("hi", b,c)
# printval