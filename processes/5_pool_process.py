from logging_utils import info, PROCESS_FORMAT
import logging
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

logging.basicConfig(level=logging.DEBUG, format=PROCESS_FORMAT)

def is_even(number):
    return number % 2 == 0, number

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=2) as executor:
        for n in range(11):
            future = executor.submit(is_even, n)
            future.add_done_callback(
                lambda future: info(f"Is {future.result()[1]} even? {future.result()[0]}")
            )