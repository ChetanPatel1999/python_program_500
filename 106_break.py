l1=[5,3,7,68,9,12,55,4,33,22]
num=int(input("enter a search num : ")) #9
for data in l1:
    if data==num:
        print("element is found")
        break
else:
    print("not found")    