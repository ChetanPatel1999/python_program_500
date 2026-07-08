#   Write a program to display factors count of given number. 
given= int(input("enter a num : ")) # 15
num=1
c=0
while num<=given:
    if given%num==0:
        c+=1        
    num+=1 

print(f"factors count = {c}")
