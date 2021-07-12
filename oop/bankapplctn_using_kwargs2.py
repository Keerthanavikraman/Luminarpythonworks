class Bank:
    users = {
        1000: {"account_num": 1000, "password": "user1", "balance": 3000},
        1001: {"account_num": 1001, "password": "user2", "balance": 4000},
        1002: {"account_num": 1002, "password": "user3", "balance": 5000},
        1003: {"account_num": 1003, "password": "user4", "balance": 6000}
    }

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
                return acc_no
            else:
                return -1   #invalid password
        else:
            return 0        #invalid account number
    def balance_enquiry(self,acc_no):
        print(self.users[acc_no]["balance"])

bank = Bank()
user=bank.authenticate(acc_no=1000, password="user1")
bank.balance_enquiry(user)
