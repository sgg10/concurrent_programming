from logging_utils import info, debug,PROCESS_FORMAT
import logging
import multiprocessing
from random import randint
from time import sleep

logging.basicConfig(level=logging.DEBUG, format=PROCESS_FORMAT)

def sai_hi(id) -> None:
    time_to_sleep = randint(1, 60)
    info(f"Hi! I'm a new process with id = {id} | Time to sleep = {time_to_sleep}")
    sleep(time_to_sleep)
    debug("End of process")

if __name__ == "__main__":
    info("Hi, I'm main process")
    for i in range(10):
        process = multiprocessing.Process(target=sai_hi, args=(i+1,), name=f"Process-SGG-{i+1}") # kwargs={"id": i+1}
        process.start()