from logging_utils import info, debug
import threading
from time import sleep

def task():
    info("We are executing a new task")
    sleep(5)
    info("We are continuing with the execution")
    sleep(5)
    info("Finished task")

def clock():
    count = 0
    while count < 60:
        sleep(1)
        count += 1
        debug(f"Time elapsed: {count}s")

if __name__=="__main__":
    thread = threading.Thread(target=task)
    thread.start()
    clock()