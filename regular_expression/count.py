#regular expression used for pattern matching
#used for validation
#re... package for pattern matching
#used in only strings

#important


import re

count=0
matcher=re.finditer (  'ab' , 'abaabbab' )  #finditer is a method to find how many matches in a regular expression
#print(matcher)
for match in matcher:
    count += 1
print( "count=" , count )


