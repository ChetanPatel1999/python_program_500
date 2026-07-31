#  Write a program to display the list elements in reverse order.
l1=[3,6,7,4,8,2]
print("list all element  : ",l1)
# print("reverse list element : ",l1[::-1])

print("reverse list element are : ",end="")

for i in range(len(l1)-1,-1,-1):# 5 4 3 2 1 0
    print(l1[i],end=" ")






