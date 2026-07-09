#Write a program to that takes a number as input and calculates the sum of 
# only its even digits.
num= int(input("enter a num : ")) #0
ans=0
while num>0:
    rem=num%10 # 3
    if rem%2==0:
        ans= ans+rem  # 8
    num= num//10 
print("sum of individual even digit : ",ans)    