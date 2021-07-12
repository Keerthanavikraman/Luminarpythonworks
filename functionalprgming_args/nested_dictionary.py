users={
    1000:{"account_num":1000,"password":"user1","balance":3000},
    1001:{"account_num":1001,"password":"user2","balance":4000},
    1002:{"account_num":1002,"password":"user3","balance":5000},
    1003:{"account_num":1003,"password":"user4","balance":6000},
}
######### i want to check 1000 exist or not
# if (1000 in users):
#     print("exist")
# else:
#     print("not exist")

######## i want to check 1000 exist or not if 1000 exist print balance of that user

# if (1000 in users):
#     print(users[1000]["balance"])
# else:
#     print("not exist")


########print password of user 1000

# if (1000 in users):
#     print(users[1000]["password"])
# else:
#     print("not exist")











#1000,user1 login success
#1000,user2 login failed


# user=int(input("enter account number"))#1000
# password=input("enter password")#test1

#check for user exist or not

# if(user in users):
#     if(password==users[user]["password"]):
#         print("success")
#     else:
#         print("ivalid password")
# else:
#     print("invalid account number")

def authenticate(user,password):

    if(user in users):
        if(password==users[user]["password"]):
           print("success")
        else:
           print("ivalid password")
    else:
        print("invalid account number")
authenticate(1000,"user1")
#authenticate(user=1000,password="user1")

#print balance
def get_balance(accno):
    if accno in users:
        print(users[accno]["balance"])
    else:
        print("invalid account number")

get_balance(1000)
