from logging_utils import info, debug,PROCESS_FORMAT
import logging
import multiprocessing
from random import randint
from time import sleep

logging.basicConfig(level=logging.DEBUG, format=PROCESS_FORMAT)

def sai_hi(id) -> None:
    iteration = 0
    while True:
        iteration += 1
        info(f"Hi! I'm a new process with id = {id}")
        sleep(2)
        debug(f"End of iteration {iteration} in process {id}")

if __name__ == "__main__":
    info("Hi, I'm main process")
    for i in range(2):
        process = multiprocessing.Process(target=sai_hi, kwargs={"id": i+1}, name=f"Process-SGG-{i+1}", daemon=True)
        process.start()
    sleep(60)