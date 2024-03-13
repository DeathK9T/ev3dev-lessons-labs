import threading
import time

def work():
    print(f'Child thread native id: {threading.get_native_id()}')
    time.sleep(400)

# ps -eLo pid,tid,psr,args | grep thread_native_id.py
if __name__ == "__main__":  

    # start threadsCount threads
    threads = []
    threadsCount = 10
    print(f'Parent thread native id: {threading.get_native_id()}')

    for _ in range(threadsCount):
        t = threading.Thread(target=work)
        t.start()
        threads.append(t)
  
    for t in threads:
        t.join()
