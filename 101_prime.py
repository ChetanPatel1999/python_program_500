#wap to check given number is prime or not
n = int(input("enter a num : ")) # 15
c=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1

if c==2:
    print("num is prime becase its factors count = ",c)
else:
    print("num is not prime becase its factors count = ",c)    