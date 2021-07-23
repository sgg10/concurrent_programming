from logging_utils import info, PROCESS_FORMAT
import logging
import multiprocessing
from multiprocessing.managers import Namespace
from time import sleep

logging.basicConfig(level=logging.DEBUG, format=PROCESS_FORMAT)

def get_valor(namespace: Namespace) -> None:
    while namespace.sgg is None:
        info("sgg don't have a value")
        sleep(0.5)
    else:
        info(namespace.sgg)

def set_valor(namespace: Namespace) -> None:
    sleep(4)
    namespace.sgg = "Sebastian Granda Gallego"

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    namespace = manager.Namespace()

    namespace.sgg = None

    p1 = multiprocessing.Process(target=get_valor, args=(namespace, ))
    p2 = multiprocessing.Process(target=set_valor, args=(namespace, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()