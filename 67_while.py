#  Write a program to display number square 1 to n (given number).
given=int(input("enter ending range : "))# 5
num=1
while num<=given:
    print(f"square of {num} = {num*num}")
    # print("square of", num ,"=", num*num)
    num=num+1  