#  Write a program to take input and print all elements of list. 

l1=[]
n = int(input("enter list length : ")) # 5
for i in range(n): # 0 1 2 3 4
    num = int(input(f"enter list element{i+1} : "))
    l1.append(num)

print("list element are : ")
for ele in l1:
    print(ele,end=" ")