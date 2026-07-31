# Write a program to take some student name form user and store in list. 
students=[]
n = int(input("enter list length : ")) # 5
for i in range(n): # 0 1 2 3 4
    name = input(f"enter name student{i+1} : ")
    students.append(name)

print("list element are : ")
for name in students:
    print(name,end=" ")