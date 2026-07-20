for i in range(1,6): # 4
    for j in range(i,0,-1): #4 3 2 1
        if j%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")    
    print()   

"""
 0
 1 0
 0 1 0
 1 0 1 0
 0 1 0 1 0 

"""    