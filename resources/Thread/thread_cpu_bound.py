import threading
import time
import math

# cpu-bound нагрузка
def sum_sin(n):
    sum = 0
    pi = 3.1415926535
    for i in range(n):
        sum += math.sin(i * 2 * pi / n)
    return sum

def work():
    n = 10_000_000
    start = time.time()
    res = sum_sin(n)
    duration = time.time() - start
    print(f'Duration: {round(duration,4)}, result: {res}')

if __name__ == "__main__":  
    threads = []
    threadsCount = 5

    for _ in range(threadsCount):
        t = threading.Thread(target=work)
        t.start()
        threads.append(t)
  
    for t in threads:
        t.join()
