import datetime
import threading
import time

semphore = threading.Semaphore(2)

def semaphore_func(payload: int):
    with semphore:
        now = datetime.datetime.now().strftime('%H:%M:%S')
        print(f'{now=}, {payload=}')
        time.sleep(1)

if __name__ == "__main__":  
    threads = [threading.Thread(target=semaphore_func, args=(i,)) for i in range(5)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()