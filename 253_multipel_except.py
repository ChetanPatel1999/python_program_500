print("this is division app :")
l1=[34,56,78,45,39]
try: 
  a=int((input("enter a : "))) #12
  b=int((input("enter b : ")))  # 6
  c=a/b
  print("division : ",c)
  index=int((input("enter index : "))) #9
  print("elemen at index : ",l1[index])
except ZeroDivisionError:
  print("zero division error")  
except IndexError as e:
  print(e)  
except ValueError:
  print("wrong input")  
except:
  print("someting is wrong")  
print("division program run succefully")

print("this is addition app :")
a=int((input("enter a : ")))
b=int((input("enter b : ")))
c=a+b
print("addition : ",c)
print("addition program run succefully")