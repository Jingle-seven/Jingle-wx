import threading
import time

def printTime(delayTime,threadName):
    print(threadName,"start")
    while(True):
        print(threadName,time.ctime())
        time.sleep(delayTime)
        
print("start")
t1 = threading.Thread(target=printTime,args=(2,"t1"))
t2 = threading.Thread(target=printTime,args=(3,"t2"))
t1.start()
t2.start()
print("end")


                                    
        

