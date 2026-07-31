# Write a program to find the sum of all elements in an list. 
l1=[3,6,4,7,8,9]

print("list : ",l1)
sum=0

for ele in l1:
    sum=sum+ele # 13

print("sum of list element is = ",sum)
print("average of list element is = ",sum/len(l1))

if sum%2==0:
    print("sum is even")
else:
    print("sum is odd")    


