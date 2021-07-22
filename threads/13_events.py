from logging_utils import info, debug, THREAD_FORMAT
import logging
import threading
from time import sleep

logging.basicConfig(level=logging.DEBUG, format=THREAD_FORMAT)

def thread_1(event: threading.Event) -> None:
    info("I'm waiting for a signal")

    event.wait()

    info("Signal was receive, the event flag is true")

def thread_2(event: threading.Event) -> None:
    while not event.is_set(): # It runs until the signal is sent
        debug("I'm waiting for a signal")
        sleep(0.5)

if __name__ == "__main__":

    event = threading.Event()

    thread1 = threading.Thread(target=thread_1, args=(event, ))
    thread2 = threading.Thread(target=thread_2, args=(event, ))

    thread1.start()
    thread2.start()

    sleep(3)

    event.set() # We are sending a signal

    event.clear() # Set signal to false
