#  Write a program to display sum 1 to n ( given number). 
given=int(input("enter a num : "))#5
num=1
res=0
while num<=given:
    res=res+num   
    num+=1 
print(f"sum of 1 to {given} = {res}")    
print(f"average of 1 to {given} = {res/given}")    
