# Write a program to reverse a string.
# s= input("enter a string : ")
# print("string : ",s) # ram
# revstr= s[::-1]
# print("string reverse: ",revstr)


s= input("enter a string : ")
print("string : ",s) # ram
revstr= ""

for i in range(len(s)-1,-1,-1): # 2 1 0
    revstr=revstr+s[i] # ma

print("string reverse: ",revstr)
