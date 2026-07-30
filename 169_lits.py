# how to iterate list element
l1=[12,34,56,78,90]

print("list element are : ")
for ele in l1:
    print(ele)


print("second way to iterate list element : ")  

for i in range(len(l1)):
    print(l1[i])


print("third way to iterate list element : ")
i=0
while i<len(l1):
    print(l1[i])  
    i+=1 # 2
