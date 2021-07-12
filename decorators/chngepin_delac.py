def admin_required(func):
    def wrapper(user,pin):   #(a,b)
        if user!='admin':    #a!
            raise Exception("you are not allowed")
        else:
            return func(user,pin)  #(a,b)
    return wrapper

@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin
@admin_required
def delete_ac(user,pin):
    return str(acno)+"delete"
print(change_pin("admin",1000))
#print(delete_ac("user",1000))