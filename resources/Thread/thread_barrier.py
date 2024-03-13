from threading import Barrier
from threading import Thread
import time
import random

def client(bar: Barrier) -> None:
    time.sleep(random.uniform(0,1))
    id_local = bar.wait()
    print(f'id_local: {id_local}')
    
if __name__ == "__main__":  
    parties = 4
    barrier = Barrier(parties)

    threads = []
    threadsCount = parties * 3

    for _ in range(threadsCount):
        t = Thread(target=client)
        t.start()
        threads.append(t)
  
    for t in threads:
        t.join()
