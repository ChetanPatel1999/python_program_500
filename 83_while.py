#  Write a program that takes a number as input and counts how many even 
# digits it contains.

num= int(input("enter a num : ")) #3425
ans=0
while num>0:
    rem=num%10
    if rem%2==0:
       ans= ans+1
    num= num//10  
print("total even digit count in number = " ,ans) 