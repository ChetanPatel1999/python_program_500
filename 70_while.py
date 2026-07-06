#  Write a program to display multiple of   7  between given range. 
num=int(input("enter start range  : ")) # 10
given= int(input("enter end range : ")) # 20
while num<=given:
    if num%7==0:
        print(num,end=" ") # 4
    num+=1 # 11