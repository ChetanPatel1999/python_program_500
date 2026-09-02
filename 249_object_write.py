#how to write object in file
# dump() :- we use dump method to write data in file
from pickle import dump
l1=[12,34,56,67]
d1={"hello":45,"math":90}
file= open(r"C:\Users\PC\Desktop\Demo\palak.txt","wb")
dump(l1,file)
dump(d1,file)
file.close()