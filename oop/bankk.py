# class Bank:
#     def setval(self,fixed_amount,withdraw,ac_nbr):
#         self.fixed_amount=fixed_amount
#         self.withdraw=withdraw
#         self.ac_nbr=ac_nbr
#
#
#     def printval(self):
#         print(self.fixed_amount-self.withdraw,self.ac_nbr)
#         print(self.withdraw<self.fixed_amount)
#         print(self.withdraw > self.fixed_amount)
# bank1=Bank()
# bank1.setval(10000,1000,"SBI00700312345")
# bank1.printval()


class Bank:
    def acCreate(self, acno,name,bname):
        self.acno=acno
        self.name=name
        self.bname=bname
        self.minimumbal=5000
        self.balance=self.minimumbal
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print("your",self.bname,"account has been credited with amount",self.amount)
        print("your current balance",)
        print("your current balance=",self.balance)
    def withdraw(self,amount):
        self.amount=amount
        if self.amount>self.balance:
            print("insufficient balance")
        else:
            print("account debited with",self.amount)
            self.balance=self.balance-self.amount
            print("available balance=",self.balance)
obj=Bank()
num=int(input("enter ac num"))
obj.acCreate(num,'abc',"sbi")
obj.deposit(2500)
obj.withdraw(1500)