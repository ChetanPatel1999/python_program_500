#Write a program to display factors of given number.
# 12 -> 1 2 3 4 6 12
# 15 -> 1 3 5 15

n = int(input("enter a num : "))
print(f"factors of {n} = ",end="")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")



