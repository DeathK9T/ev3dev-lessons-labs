import threading
import time
import argparse
import random

# io-bound нагрузка
# чтения данных с датчика
def read_data():
    time.sleep(1)
    return random.uniform(0, 1)

def work():
    start = time.time()
    ret = read_data()
    duration = time.time() - start
    print(f'Duration: {round(duration,5)}, result: {round(ret,4)}')

if __name__ == "__main__":  
    parser = argparse.ArgumentParser(description='IO-bound tasks')
    parser.add_argument('--n_threads', '-n', type=int, default=1, help='Number of threads')
    args = parser.parse_args()
    
    threadsCount = args.n_threads
    threads = []
    for _ in range(threadsCount):
        t = threading.Thread(target=work)
        t.start()
        threads.append(t)
  
    for t in threads:
        t.join()
