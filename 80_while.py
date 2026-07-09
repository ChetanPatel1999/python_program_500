#  Write a program to takes a number as input and calculates the sum of its 
# individual digits. 
num= int(input("enter a num : ")) # 345
ans=0
while num>0:
    rem=num%10 
    ans= ans+rem 
    num= num//10 
print("sum of individual digit : ",ans)    