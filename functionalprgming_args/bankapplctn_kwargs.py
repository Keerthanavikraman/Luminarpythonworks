users={
    1000:{"account_num":1000,"password":"user1","balance":3000},
    1001:{"account_num":1001,"password":"user2","balance":4000},
    1002:{"account_num":1002,"password":"user3","balance":5000},
    1003:{"account_num":1003,"password":"user4","balance":6000},
    1004:{"account_num":1004,"password":"user5","balance":7000}
}



def authenticate(**kwargs):  #kwargs{"accno":1000,"password":test1}    ###kwargs function accept any number of arguments
    user=kwargs["user"]
    password=kwargs["password"]
    if (user in users):
        if (password == users[user]["password"]):
           print("success")
        else:
           print("ivalid password")
    else:
        print("invalid account number")


#print balance
def get_balance(accno):
    if accno in users:
        print(users[accno]["balance"])
    else:
        print("invalid account number")

authenticate(accno=1000,password="test1")
authenticate(accno=1000,password="user1")

#accno=int(input("enterr"))
#authenticate(accno=accno,password="user1")



