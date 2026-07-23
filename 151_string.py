#wap to count no of only even digit in given number.
num=int(input("enter a number : "))# 7895
num= str(num)
c=0
for n in num:
    if int(n) % 2==0:
        c+=1
print("even digit count = ",c)        


