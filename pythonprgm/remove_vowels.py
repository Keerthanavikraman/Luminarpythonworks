a="a e i o u A E I O U"
b=input("enter the string")
no_vowels=""
for i in b:
    if i not in a:
        no_vowels=no_vowels+i
print(no_vowels)
