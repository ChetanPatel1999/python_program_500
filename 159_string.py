#Write a program to check whether a string is a palindrome or not.
#naman
#saloni
#madam
#malayalam
#mom

s= input("enter a string : ") # naman
revstr=""

for ch in s:
    revstr=ch+revstr 
      
if s==revstr:
    print("string is plindrom")
else:
        print("string is not plindrom")    

