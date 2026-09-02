#how to read objet from file
from pickle import load
file= open(r"C:\Users\PC\Desktop\Demo\palak.txt","rb")
l1=load(file)
d1=load(file)
print(l1)
print(d1)
file.close()