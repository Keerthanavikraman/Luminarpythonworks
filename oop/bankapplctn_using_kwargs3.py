class Bank:
    users = {
        1000: {"account_num": 1000, "password": "user1", "balance": 3000},
        1001: {"account_num": 1001, "password": "user2", "balance": 4000},
        1002: {"account_num": 1002, "password": "user3", "balance": 5000},
        1003: {"account_num": 1003, "password": "user4", "balance": 6000}
    }
    session={}
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
    def balance_enquiry(self,acc_no):
        if (acc_no==self.session["user"]):

            print(self.users[acc_no]["balance"])
        else:
            print("you must login")

bank = Bank()
user=bank.authenticate(acc_no=1000, password="user1")
bank.balance_enquiry(user)


# bank1 = Bank()
# bank1.authenticate(acc_no=1001, password="user2")
# bank1.balance_enquiry(1001)

bank1 = Bank()
user=bank1.authenticate(acc_no=1001, password="user2")
bank1.balance_enquiry(user)



bank1 = Bank()
user=bank1.authenticate(acc_no=1001, password="user3")
if (user==-1)|( user==0):
    print("authentication failed")
else:
    bank1.balance_enquiry(user)
