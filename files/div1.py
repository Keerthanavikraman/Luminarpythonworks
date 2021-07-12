# num1=int(input("enter no1"))
# num2=int(input("enter no2"))
# print(num1/num2)

#num1=5,num2=0 unexpected errors - to solve this try except  are used
#exception handling- to solve unexpected errors
#try....exceptional code                    #works everytime
#except....solving code after exception    #works during errors
#finally....anything can be given ,it works


num1=int(input("enter no1"))  #5
num2=int(input("enter no2"))  #0
try:
    print(num1/num2)          #5/0 #error ,control goes to except
except:
    print("exception occured")
finally:
    print("inside finally")


num1=int(input("enter no1"))  #5
num2=int(input("enter no2"))  #0
try:
    print("hello")
    print(num1/num2)          #5/0 #error ,control goes to except
except Exception as e:
    print("exception occured",e)
finally:
    print("inside finally")


