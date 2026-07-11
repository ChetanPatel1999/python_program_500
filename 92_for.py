# Write a program to display number square 1 to n (given number). 
given = int(input("enter a num : ")) # 5
for num in range(1,given+1): # (1,2,3,4,5)
    print(f"squre of {num} = {num*num}")