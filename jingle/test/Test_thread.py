import _thread
import time

def printTime(delayTime,threadName):
    print(threadName,"start")
    while(True):
        print(threadName,time.ctime())
        time.sleep(delayTime)
        
print("start")
_thread.start_new_thread(printTime, (2,"t1"))
_thread.start_new_thread(printTime, (3,"t2"))
print("end")


                                    
        

