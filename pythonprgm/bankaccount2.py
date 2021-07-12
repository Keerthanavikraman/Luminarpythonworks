fixed_amount= 10000
a=int(input("enter the amount to withdraw"))
print("ac balance",fixed_amount-a)
if a<fixed_amount:
    print(" sufficient balance")
else:
    print("insufficient balance")