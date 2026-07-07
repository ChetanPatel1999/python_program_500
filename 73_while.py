#  Write a program to display sum 1 to n ( given number). 
given=int(input("enter a num : "))#5
num=1
res=0
while num<=given:
    res=res+num 
    if num==given:
        print(num,end="")
    else:
        print(num,end=" + ")    
    num+=1  #6
print(" = ",res)    



# 1 + 2 + 3 + 4 + 5 = 15 
