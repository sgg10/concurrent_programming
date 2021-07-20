from logging_utils import info, THREAD_FORMAT
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format=THREAD_FORMAT)

BALANCE = 0

def deposit() -> None:
    global BALANCE
    for _ in range(0, 1000000):
        BALANCE += 10

def withdrawal() -> None:
    global BALANCE
    for _ in range(0, 1000000):
        BALANCE -= 10

if __name__ == '__main__':
    thread1 = threading.Thread(target=deposit)
    thread2 = threading.Thread(target=withdrawal)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    info(f"Total balance: {BALANCE}")
