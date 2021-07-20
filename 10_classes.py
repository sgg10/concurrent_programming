from typing import Optional
from logging_utils import info, debug, THREAD_FORMAT
import logging
import threading
from time import sleep

logging.basicConfig(level=logging.DEBUG, format=THREAD_FORMAT)

class ThreadSGG(threading.Thread):
    def __init__(self, name: Optional[str]=None, daemon: Optional[bool]=False) -> None:
        threading.Thread.__init__(self, name=name, daemon=daemon)

    def run(self) -> None:
        while True:
            info("Custom Thread Class")
            sleep(1)

if __name__ == "__main__":
    thread = ThreadSGG(daemon=True, name="Thread-SGG")
    thread.start()

    sleep(3)
    debug("Script Finish")