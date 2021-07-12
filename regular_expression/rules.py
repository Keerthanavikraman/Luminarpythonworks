#x='[abc]' either a b or c
#x='[^abc]' except abc
#x='[a-z]' a to z
#x='[A-Z]' A to Z
#x='[a-zA-Z]' both lower and upper case are checked
#x='[0-9]' check digits
#x='[^a-zA-Z0-9]' special symbols
#x='\s' check space
#x='\d' check digits
#x='\D' except digits
#x='\w' all words except special characters
#x='\W' for special characters



# import re
# x="[abc]" # either a,bor c
# matcher=re.finditer (  x , "abt c@5kzabc" )
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
# x='[^abc]' #except abc
# matcher=re.finditer (  x , "abt c@5kzabc" )
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x = '[a-z]'  #a to z
# matcher = re.finditer(x, "abt c@5kzabc")
# for match in matcher:
#     print(match.start())
#     print(match.group())


import re

# x = '[A-Z]'  #A to Z
# matcher = re.finditer(x, "abt c@5kAz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#

# import re
#
# x = '[a-zA-Z]'
# matcher = re.finditer(x, "abt c@5kAz")
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x = '[0-9]'   #check digits
# matcher = re.finditer(x, "abt c@5kAz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
# import re
#
# x = '[^0-9]'   #except digits
# matcher = re.finditer(x, "abt c@5kAz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#


# import re
#
# x = '[^a-zA-Z0-9]'   #special symbols
# matcher = re.finditer(x, "abt c@5kAz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
# import re
#
# x = '\s'   #check space
# matcher = re.finditer(x, "abt c@5kAz")
# for match in matcher:
#     print(match.start())
#     print(match.group())



# import re
#
# x = '\s'   #check space
# matcher = re.finditer(x, "abt c@5kAz")
# for match in matcher:
#     print(match.start())
#     print(match.group())


# import re
#
# x = '\d'   #check digits
# matcher = re.finditer(x, "abt c@5kAz")
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x = '\D'   #except digits
# matcher = re.finditer(x, "abt c@5kAz")
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x = '\w' #all words except special characters
# matcher = re.finditer(x, "abt c@5kAz")
# for match in matcher:
#     print(match.start())
#     print(match.group())

# import re
#
# x = '\W'   #for special characters
# matcher = re.finditer(x, "abt c@5kAz")
# for match in matcher:
#     print(match.start())
#     print(match.group())
#
#



