# quantifiers

#x='a+' a including group
#x='a*' count including zero number of a
#x='a?' count a as each including zero no of a
#x='a{2}' 2 no of a position
#x='a{2,3}' minimum 2 a and maximum 3 a
#x='^a' check starting with a
#x='a$' check ending with a


import re
x="a+" #count including zero number of a
r="aaa abc aaaa cga"
matcher=re.finditer (  x , r )
for match in matcher:
    print(match.start())
    print(match.group())





#import re
# x="a*" #count including zero number of a
# r="aaa abc aaaa cga"
# matcher=re.finditer (  x , r )
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# x='a?' #count a as each including zero no of a
# r="aaa abc aaaa cga"
# matcher=re.finditer (  x , r )
# for match in matcher:
#     print(match.start())
#     print(match.group())
#

#
# import re
# x='a{2}' #2 no of a position
# r="aaa abc aaaa cga"
# matcher=re.finditer (  x , r )
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# x='a{2,3}' #minimum 2 a and maximum 3 a
# r="aaa aa abc aaaaa cga"  #first takes maximum and then only takes minimum
# matcher=re.finditer (  x , r )
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
# x='a{1,3}' #minimum 2 a and maximum 3 a
# r="aaa aa abc aaaaa cga"
# matcher=re.finditer (  x , r )
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
# x='^a' #check starting with a
# r="aaa abc aaaa cga"
# matcher=re.finditer (  x , r )
# for match in matcher:
#     print(match.start())
#     print(match.group())



import re
x='a$' #check ending with a
r="aaa abc aaaa cga"
matcher=re.finditer (  x , r )
for match in matcher:
    print(match.start())
    print(match.group())

