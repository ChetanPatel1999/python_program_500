#wap to check how many vovel in string
s=input("enter a string : ")
c=0
for ch in s:
    if ch in "aeiou":
        c=c+1 # 2

print("string : ",s)
print("total vovels in string : ",c)


