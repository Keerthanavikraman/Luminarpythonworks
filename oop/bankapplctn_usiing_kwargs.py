users={
    1000:{"account_num":1000,"password":"user1","balance":3000},
    1001:{"account_num":1001,"password":"user2","balance":4000},
    1002:{"account_num":1002,"password":"user3","balance":5000},
    1003:{"account_num":1003,"password":"user4","balance":6000}
}

#authenticate(accno,password)
####balance_enquiry()    #snakenotation #python        #camlin notation #java balanceEnquiry()
#balance_enquiry(accno)
#fund_transfer(accno,toaacno,amount)



class Bank:
    users = {
        1000: {"account_num": 1000, "password": "user1", "balance": 3000},
        1001: {"account_num": 1001, "password": "user2", "balance": 4000},
        1002: {"account_num": 1002, "password": "user3", "balance": 5000},
        1003: {"account_num": 1003, "password": "user4", "balance": 6000}
    }

    def validate_account(self,accno):
        if accno in self.users:
            return True
        else:
            return False
    def authenticate(self,**kwargs):     ##kwargs={acc_no:1000,password:test}
        acc_no=kwargs["acc_no"]
        password=kwargs["password"]
        user=self.validate_account(acc_no)
        if user:
            pass
        else:
            print("invalid account number")
bank=Bank()
bank.authenticate(acc_no=1009,password="user1")

