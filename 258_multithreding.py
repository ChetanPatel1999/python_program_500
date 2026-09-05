import time
import threading
def table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")
        time.sleep(0.5)

# table(3)
# table(8)
# table(9)

t1= threading.Thread(target=table,args=[2])
t2= threading.Thread(target=table,args=[8])
t3= threading.Thread(target=table,args=[9])

# t1.start()
# t2.start()
# t1.join() # belove program run after t1 thread complete
# t3.start()



t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print("all thread run succefully")