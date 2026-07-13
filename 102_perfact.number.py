# . Write a program to check given number is perfact or not.
n = int(input("enter a num : ")) # 12
sum=0
for i in range(1,n+1):
    if n%i==0:
        sum=sum+i # 

if sum == n*2:
    print("num is perfact")
else:
    print("num is not perfact")    
