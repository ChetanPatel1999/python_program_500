# split():- its seprate all world of string and create a list then return list

# s="indore is a clean city"

# l1= s.split()

# for word in l1:
#     print(word)


# #wap to print how many character present in string each word.
# s="indore is clean city"
# l1= s.split()
# for w in l1:
#     print(f"{w} = {len(w)}")


# wap to reavese each word in string
s="indore is a clean city"
# erodni  si  a  naelc  ytic
rev=""
print(s)
l1= s.split()
for w in l1:
    rev= rev + w[::-1]+" "

print(rev)

# for i in range(len(l1)-1 , -1 , -1): # 4 3 2 1 0
#     print(l1[i],end=" ")

#indore is a clean city
n=""
for w in l1:
    n = w+" " + n

print(n)





