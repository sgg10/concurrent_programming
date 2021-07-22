from logging_utils import info, THREAD_FORMAT
import logging
import threading
import queue
from random import randint
from time import sleep

logging.basicConfig(level=logging.DEBUG, format=THREAD_FORMAT)

"""
Producer - Consumer problem.

Th program describe two processes: producer and consumer,
both of them share a finite size buffer.
Producer task is generate a product, store it and start again.
While consumer takes (simultaneously) products one by one.
The problem is that the producer does not add more products than the buffer capacity
and that the consumer does not try to take a product if the buffer is empty.
"""

queue = queue.Queue(maxsize=10)

def producer():
    while True:
        if not queue.full():
            item = randint(1, 100)
            queue.put(item)
            info(f"[Producer] New element into queue: {item}")
            sleep(randint(1, 3))


def consumer():
    while True:
        if not queue.empty():
            item = queue.get()
            queue.task_done()
            info(f"[Consumer] New element obtained: {item}")
            sleep(randint(1, 3))

if __name__ == "__main__":
    thread_producer = threading.Thread(target=producer)
    thread_consumer = threading.Thread(target=consumer)

    thread_producer.start()
    thread_consumer.start()