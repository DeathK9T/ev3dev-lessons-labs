from time import sleep
from random import random
from threading import Thread
from threading import Condition
from threading import Event

# target function
def task(condition: Condition, event: Event, number: int) -> None:
    
    # wait to be notified
    print(f'Thread {number} waiting...')
    with condition:
        # для примера lambda, можно передать event.is_set
        condition.wait_for(lambda local_event=event: local_event.is_set())

    # block for a moment
    value = random()
    sleep(value)
    # report a result
    print(f'Thread {number} got {value}')

if __name__ == "__main__":
    # create a condition
    condition = Condition()
    # create a event
    event = Event()

    workers = []
    # start a bunch of threads that will wait to be notified
    for i in range(5):
        worker = Thread(target=task, args=(condition, event, i))
        worker.start()
        workers.append(worker)

    # notify all waiting threads that they can run
    with condition:
        # wait to be notified
        event.set()
        condition.notify_all()

    # block until all non-daemon threads finish...
    for worker in workers:
        worker.join()