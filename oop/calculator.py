class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+ self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def divi(self):
        return self.a / self.b

a=int(input("enter"))
b=int(input("enter"))
obj=Calculator(a,b)
print(obj.add())
print(obj.sub())
print(obj.mul())
print(obj.divi())


