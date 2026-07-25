#reaplace any char only frist appearenece
s="indore is clean city"
old="e"
new="p"
newstr=""
f=0
for ch in s:
    if ch==old and f != 1:
        newstr=newstr+new 
        f=1
    else:
        newstr=newstr+ch    

print(s)        
print(newstr)        