from logging_utils import info, debug,PROCESS_FORMAT
import logging
import multiprocessing
from random import randint
from time import sleep

logging.basicConfig(level=logging.DEBUG, format=PROCESS_FORMAT)

def sai_hi(id) -> None:
    info(f"Hi! I'm a new process with id = {id}")
    sleep(30)
    info("End of child process")

if __name__ == "__main__":
    process = multiprocessing.Process(target=sai_hi, kwargs={"id": 1}, name=f"Process-SGG-{1}")
    process.start()

    sleep(2)

    if process.is_alive():
        process.terminate()
        info("Child process terminated prematurely")
