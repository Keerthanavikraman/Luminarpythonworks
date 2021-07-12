def login_required(func):
    def wrapper(self,acno,*args,**kwargs):
        if(self.session["user"]==acno):
            func(self,acno,*args,**kwargs)
        else:
            raise Exception("u must login")
    return wrapper

class Bank:
    users = {
        1000: {"account_num": 1000, "password": "user1", "balance": 3000},
        1001: {"account_num": 1001, "password": "user2", "balance": 4000},
        1002: {"account_num": 1002, "password": "user3", "balance": 5000},
        1003: {"account_num": 1003, "password": "user4", "balance": 6000}
    }
    session={}
    session["user"]=0
    def validate_account(self, accno):
        if accno in self.users:
            return True
        else:
            return False

    def authenticate(self, **kwargs):  ##kwargs={acc_no:1000,password:test}
        acc_no = kwargs["acc_no"]
        password = kwargs["password"]
        user = self.validate_account(acc_no)
        if user:
            if password==self.users[acc_no]["password"]:
                self.session["user"]=acc_no    #session{user:1000}
                return acc_no
            else:
                return -1   #invalid password
        else:
            return 0        #invalid account number

    @login_required
    def balance_enquiry(self,acc_no,*args,**kwargs):
        print(self.users[acc_no]["balance"])

    @login_required
    def fund_transfer(self,user,to_accno,amt):
         if self.validate_account(to_accno):
             balance=self.users[user]["balance"]     #balance=self.balance_enquiry(user)
             if balance<amt:
                print("insufficient balance")
             else:
                 self.users[user]["balance"]-=amt
                 self.users[to_accno]["balance"]+=amt
    def logout(self):
        self.session["user"]=0


# bank1 = Bank()
# user=bank1.authenticate(acc_no=1001, password="user2")
# if (user==-1)|( user==0):
#     print("authentication failed")
# else:
#     bank1.balance_enquiry(user)
# bank1.fund_transfer(user,1002,2000)
# bank1.balance_enquiry(user)
# bank1.logout()

bank2=Bank()
bank2.