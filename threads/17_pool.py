from typing import Union
from logging_utils import info, THREAD_FORMAT
import logging
import threading
from time import sleep
from random import randint

from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format=THREAD_FORMAT)

def math_operation(a: Union[int, float], b: Union[int, float]) -> None:
    sleep(1)
    info(f"{a} + {b} = {a+b}")

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5, thread_name_prefix="SGG") as executor:
        for _ in range(10):
            executor.submit(math_operation, randint(0,50), randint(0,50))
        executor.shutdown()