#  Write a program to display sum 1 to n  ( given number) only even numbers sum.
given=int(input("enter a num : "))#5
num=1
res=0
while num<=given:
    if num%2==0:
        res=res+num   
    num+=1 #6
print(f"sum of 1 to {given} even number = {res}")    
