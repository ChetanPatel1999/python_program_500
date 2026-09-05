import time
import threading
def fileDownload(filename,second):
    print(f"{filename} is downlode start ...")
    time.sleep(second)
    print(f"{filename} is downlode complete in {second} seconds")


# fileDownload("file1",2)
# fileDownload("file2",5)
# fileDownload("file3",3)

t1=threading.Thread(target=fileDownload,args=("file 1",2))
t2=threading.Thread(target=fileDownload,args=("file 2",5))
t3=threading.Thread(target=fileDownload,args=("file 3",3))

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("all file downloded completed")