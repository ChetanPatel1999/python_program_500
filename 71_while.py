#  Write a program to display even number series.
given=int(input("enter ending range : "))# 30
num=1
while num<=given:
    if num%2==0:
        print(num,end=" ")
    num=num+1