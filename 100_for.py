#Write a program to display factors count of given number.

n = int(input("enter a num : ")) # 15
c=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1

print("total factors count = ",c)



