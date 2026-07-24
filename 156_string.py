# 6. Write a program to convert a string to uppercase.
# ram ----> RAM
# abc -----> ABC
s= input("enter a string : ")# ram123
uper=""

for ch in s:
    if ch>='a' and ch<='z':
        uper=uper + chr(ord(ch)-32)
    else:
        uper = uper + ch    

print("upper case : ",uper)

