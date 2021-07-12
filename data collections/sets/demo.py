# sets...to store elements

#refernce variables specified using curly braces,elements denoted by commas

set1={1,4,5,99,2,55,90,7,4,1,2,3,2,1}
print(set1)
print(type(set1))

#### donot allow/store duplicate elements
#### order doesnot keep

#empty set creation
s2={}
print(type(s2))

s2=set()
print(type(s2))


s2=set()
s2.add("hello")
s2.add(6)
s2.add(9.8)
s2.add(True)
print(s2)

#### set supports heterogeneous data

#set iteration
s={1,2,3,4,5,6,7,8,9,0}
print(s)
for i in s:
    print(i)


#adding
# s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
# squares = set()
# for i in s:
#     squares.add(i**2)
# print(squares)


#removing       #specified element
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(s)
s.remove(0)
print(s)

#clear       #total
# s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
# print(s)
# s.clear()
# print(s)

#del         #set
# s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
# print(s)
# s.clear()
# del s
# print(s)

#### set is mutable (updatable)

#nesting

set1={1,2,{3,4}}
print(set1)
# #### nesting is not possible in set