maths=int(input("enter the score"))
physics=int(input("enter the score"))
chem=int(input("enter the score"))
eng=int(input("enter the score"))
mala=int(input("enter the score"))
sum=maths+physics+chem+eng+mala
print("your total score is",sum)

avg =sum/5
print("your average score",avg)

if avg>=91 and avg<=100:
    print("your garde is A1")
elif avg >= 81 and avg <= 91:
    print("your garde is A2")
elif avg >= 71 and avg <= 81:
    print("your garde is B1")
elif avg >= 61 and avg <= 71:
    print("your garde is B2")
elif avg >= 51 and avg <= 61:
    print("your garde is C1")
elif avg >= 41 and avg <= 51:
    print("your garde is C2")
elif avg >= 31 and avg <= 41:
    print("your garde is D")



