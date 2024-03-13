import threading
import queue

def worker(queue_elem: queue.Queue, event_stop: threading.Event):
    while not event_stop.is_set():
        if not queue_elem.empty():
            item = queue_elem.get()
            print(f'Working on {item}')
            print(f'Finished {item}')
            queue_elem.task_done()

if __name__ == "__main__":

    queue_elem = queue.Queue(10)
    event_stop = threading.Event()

    # Turn-on the worker thread.
    thr_worker = threading.Thread(target=worker, args=(queue_elem, event_stop,))
    thr_worker.start()

    # Send thirty task requests to the worker.
    for item in range(30):
        queue_elem.put(item)

    # Block until all tasks are done.
    queue_elem.join()
    print('All work completed')
    event_stop.set()
    thr_worker.join()

