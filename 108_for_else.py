# wap to cheke no is prime or not.
num = int(input("enter a num : "))# 17

for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
else:
    print("prime number")     