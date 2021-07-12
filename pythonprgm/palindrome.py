#malayalam


# a="luminar"
# print(a[::-1])   #reverse
#                  #list concept
                # applicable to string only


# def palindrome(s):
#     return s==s[::-1]
# s="malayalam"
# ans= palindrome(s)
# if ans:
#     print("yes")
# else:
#     print("no")

a=input("enter the string")
b=a[::-1]
if a==b:
    print("palindrome")
else:
    print("not palindrome")

w=int(input("enter the string"))
a=str(w)
b=a[::-1]
if a==b:
    print("palindrome")
else:
    print("not palindrome")
