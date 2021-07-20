from logging_utils import info, THREAD_FORMAT
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format=THREAD_FORMAT)

BALANCE = 0

lock = threading.Lock()

def deposit() -> None:
    global BALANCE
    for _ in range(0, 100000):
        with lock:
            #lock.acquire()
            BALANCE += 10
            #lock.release()

def withdrawal() -> None:
    global BALANCE
    for _ in range(0, 100000):
        with lock:
            #lock.acquire()
            BALANCE -= 10
            #lock.release()

if __name__ == '__main__':
    thread1 = threading.Thread(target=deposit)
    thread2 = threading.Thread(target=withdrawal)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    info(f"Total balance: {BALANCE}")
