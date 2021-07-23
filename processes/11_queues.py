from logging_utils import info, PROCESS_FORMAT
import logging
import multiprocessing
from time import sleep

logging.basicConfig(level=logging.DEBUG, format=PROCESS_FORMAT)

def get_elements(queue) -> None:
    while not queue.empty():
        element = queue.get(block=True)
        info(element)

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    queue = manager.Queue()

    for x in range(1,21):
        queue.put(x)

    info("Queue already has element")

    p1 = multiprocessing.Process(target=get_elements, args=(queue, ))
    p2 = multiprocessing.Process(target=get_elements, args=(queue, ))
    p3 = multiprocessing.Process(target=get_elements, args=(queue, ))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    info("End")