#  Write a program to display table of given number. 
# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
given=int(input("enter a num for table print : "))
num=1
while num<=10:
    print(f"{given} x {num} = {given*num}")
    num+=1
