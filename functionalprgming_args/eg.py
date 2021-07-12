# lst=[10,4,5,6,11,12,13,56]
# lst.sort()
# print(lst)

# lst=[10,4,5,6,11,12,13,56]
# sort=sorted(lst)  #sorted function
# print(sort)  #sort method


# #reverse order
# lst=[10,4,5,6,11,12,13,56]
# lst.sort(reverse=True)
# print(lst)

# class list:
#     def sort(self):
# lst=[10,4,5,6,11,12,13,56]
# lst.sort(reverse=True)
# print(lst)


# class list:
#     def sort(self,**kwargs):          #kwargs("reverse=True)   #def sort(self,boolean):
#                                        #kwargs accept in dictionary format
# lst=[10,4,5,6,11,12,13,56]
# lst.sort(reverse=True)
# #lst.sort(reverse=True,key=lst[0])    #kwargs("reverse=True,"key"=lst[0])
# print(lst)





# class list:
#     def sort(self,**kwargs) #kwargs("reverse=True)       #key=value
#         print("inside sort")
#
# lst=[10,4,5,6,11,12,13,56]
# lst.sort(reverse=True)

# lst=[10,4,5,6,11,12,13,56]
# lst.sort(reverse=True)

# lst=[10,4,5,6,11,12,13,56]
# sort=sorted(lst)
# print(sort)

# class Bank:
#     def authenticate(self):    """method"""
#         pass
#
# def authenticated():          """function"""
#     pass

# lst=[10,4,5,6,11,12,13,56]
# srt=sorted(lst,reverse=True)
# print(srt)

# def printPerson(location,birthplace):
#     print(location)
#     print(birthplace)
# printPerson("kakkanad","thrissur")
#
# def printPerson(**kwargs):
#     print(location)
#     print(birthplace)
# printPerson(wrklctn="kakkanad",homelctn="thrissur")

#### to print worklocation

def printPerson(**dict):     ##dictionaryname=dict    ##dict={"wrklctn":"kakkanad","homelctn":"thrissur"}
    print(dict["wrklctn"])
    print(dict["homelctn"])
printPerson(wrklctn="kakkanad",homelctn="thrissur")


def printPerson(**kwargs):     ##dictionaryname=dict    ##dict={"wrklctn":"kakkanad","homelctn":"thrissur"}
    print(kwargs["wrklctn"])
    print(kwargs["homelctn"])
printPerson(wrklctn="kakkanad",homelctn="thrissur")    #kwargs accept the values as keyvalue pairs



