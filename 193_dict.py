students={
    "st1":{"name":"ram","age":10},
    "st2":{"name":"rohit","age":30},
    "st3":{"name":"mohan","age":24},
    }


# chnage value in nested dictionary
# students["st3"]["age"]=50


# delete value from nested dictionary
del students["st3"]["age"]

print(students)