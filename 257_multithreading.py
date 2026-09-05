import time
import threading
def table2():
    for i in range(1,11):
        print(f"{2} * {i} = {2*i}")
        time.sleep(0.5)

def table3():
    for i in range(1,11):
        print(f"{3} * {i} = {3*i}")
        time.sleep(0.5)

def table4():
    for i in range(1,11):
        print(f"{4} * {i} = {4*i}")
        time.sleep(0.5)        


#single threding
# table2()
# table3()
# table4()


t1= threading.Thread(target=table2)
t2= threading.Thread(target=table3)
t3= threading.Thread(target=table4)

t1.start()
t2.start()
t3.start()
