import threading
import time

def exec():
    print('Start of the thread')
    time.sleep(3)
    print('End of the thread')

def get5threads():
    threads = []
    for i in range(5):
        th = threading.Thread(target = exec)
        threads.append(th)
    return threads

def startThreadsWithDelay(threadList, delay: int = 0):
    for th in threadList:
        th.start()
        time.sleep(delay)

def joinThreads(threadList):
    for th in threadList:
        th.join()

thList = get5threads()
startThreadsWithDelay(thList)
joinThreads(thList)