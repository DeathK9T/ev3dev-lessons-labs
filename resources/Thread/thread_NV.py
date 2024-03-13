import threading
import logging
import time
import random
import os

if not os.path.isdir("log"):
     os.mkdir("log")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(f"log/{__name__}.log", mode='w')
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# cpu-bound нагрузка
def estimate_pi(n):
    num_point_circle = 0 #кол-во точек внутри круга
    num_point_total = n

    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        distance = x**2 + y**2

        if distance <= 1: #определяем, что точка попала внутрь круга
            num_point_circle += 1

    return 4 * num_point_circle/num_point_total

def work():
    n = 1_000_000
    print(f'Child thread native id: {threading.get_native_id()}')

    start = time.time()
    res = estimate_pi(n)
    duration = time.time() - start

    logger.info(f'ThreadID [{threading.get_native_id()}],  duration {round(duration,3)}, result: {round(res,3)}')

# ps -eLo pid,tid,psr,args | grep thread_native_id.py
# renice -20 -p <pid>
if __name__ == "__main__":  
    print(f'Parent thread native id: {threading.get_native_id()}')
    
    threads = []
    threadsCount = 10
    for _ in range(threadsCount):
        # попробуйте задать приоритет потока в OS
        t = threading.Thread(target=work)
        t.start()
        threads.append(t)
  
    for t in threads:
        t.join()
