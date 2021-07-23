from logging_utils import info, PROCESS_FORMAT
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format=PROCESS_FORMAT)

def deposit(namespace, lock) -> None:
    for _ in range(0, 1000):
        lock.acquire()
        namespace.balance += 10
        lock.release()

def withdrawal(namespace, lock) -> None:
    for _ in range(0, 1000):
        with lock:
            namespace.balance -= 10

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    lock = manager.Lock()

    namespace = manager.Namespace()
    namespace.balance = 0

    p1 = multiprocessing.Process(target=deposit, args=(namespace, lock))
    p2 = multiprocessing.Process(target=withdrawal, args=(namespace, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    info(f"Balance: {namespace.balance}")
