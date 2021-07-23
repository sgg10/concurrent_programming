from logging_utils import info, debug,PROCESS_FORMAT
import logging
import multiprocessing
from random import randint
from time import sleep

logging.basicConfig(level=logging.DEBUG, format=PROCESS_FORMAT)

def sai_hi(id) -> None:
    info(f"Hi! I'm a new process with id = {id}")
    sleep(5)

if __name__ == "__main__":
    info("Hi, I'm main process")
    process = multiprocessing.Process(target=sai_hi, kwargs={"id": 1}, name=f"Process-SGG-{1}")
    process.start()
    process.join()
    info("Final message")