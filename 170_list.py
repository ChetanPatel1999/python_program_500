#  Write a program to take input and print all elements of list. 

l1=[]
n = int(input("enter list length : ")) # 5
for i in range(n):
    num = int(input("enter list element : "))
    l1.append(num)

print("list element are : ")
for ele in l1:
    print(ele,end=" ")