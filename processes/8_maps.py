from logging_utils import info, PROCESS_FORMAT
import logging
import multiprocessing
# from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Pool
from time import sleep


logging.basicConfig(level=logging.DEBUG, format=PROCESS_FORMAT)

def is_even(number):
    sleep(1)
    return number % 2 == 0, number

def show_result(results):
    info(f"Result: {results}")

if __name__ == "__main__":
    with Pool(processes=2) as executor:
        numbers = [ n for n in range(1, 15) if n % 2 == 0]
        # list_result = executor.map(is_even, numbers)
        # info(f"Result: {list_result}")
        map_result = executor.map_async(is_even, numbers, callback=show_result)

        info("Waiting for results...")

        map_result.wait()
        #info(f"Result: {map_result.get()}")

        for element in executor.imap_unordered(is_even, numbers): # Generator
            info(f"{element}")

