from logging_utils import info, THREAD_FORMAT
import logging
import threading
import queue
from time import sleep

logging.basicConfig(level=logging.DEBUG, format=THREAD_FORMAT)

def show_elements(queue: queue.Queue) -> None:
    while not queue.empty():
        item = queue.get()

        info(f"The element is: {item}")

        queue.task_done()

        sleep(0.5)

if __name__ == "__main__":
    my_queue = queue.Queue() # FIFO

    for val in range(20):
        my_queue.put(val)

    info("Queue already has elements!")

    for _ in range(4):
        threading.Thread(target=show_elements, args=(my_queue, )).start()