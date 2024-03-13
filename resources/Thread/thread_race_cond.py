import threading
import time

class Counter:
    def __init__(self):
        self._val = 0
  
  # change "self.val += 1" "self.val += int(1)"
    def change(self):
        self._val += int(1)

    def get_val(self):
        return self._val

# working with a shared variable
def work(counter, operationsCount):
    for _ in range(operationsCount):
        counter.change()


if __name__ == "__main__":  
    # shared variable
    counter = Counter()

    # start threadsCount threads
    threads = []
    threadsCount = 10
    operationsPerThreadCount = 1000000

    start = time.monotonic()
    for _ in range(threadsCount):
        t = threading.Thread(target=work, args=(counter, operationsPerThreadCount,))
        t.start()
        threads.append(t)
  
    for t in threads:
        t.join()
    duration = time.monotonic() - start

    expectedCounterValue = threadsCount * operationsPerThreadCount
    print(f"Expected val: {expectedCounterValue}, actual val: {counter.get_val()}")
    print(f'Duration: {round(duration, 4)}')