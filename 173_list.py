# Write a program to display all even numbers present in an list.
l1=[3,66,7,4,8,67,12]
print("list all element  : ",l1) 

print("only even element : ",end="")
for ele in l1:
    if ele%2==0:
        print(ele,end=" ")

