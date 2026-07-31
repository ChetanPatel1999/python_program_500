# . Write a program to count how many even numbers are present in an list.
l1=[3,66,7,4,8,67,12,45,28]
print("list all element  : ",l1)  

c=0
for ele in l1:
    if ele % 2 ==0:
        c=c+1

print(f"total even element count : {c}")