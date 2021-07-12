#match.start... return positions
#match.group..which object find match



import re

count=0
matcher=re.finditer (  'ab' , 'abaabbab' )  #finditer is a method to find how many matches in a regular expression
#print(matcher)
for match in matcher:
    print("match available at",match.start())
    print("group=",match.group())
    count += 1
print( "count=" , count )

