from logging_utils import info, PROCESS_FORMAT
import logging
import multiprocessing
# from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Pool


logging.basicConfig(level=logging.DEBUG, format=PROCESS_FORMAT)

def is_even(number):
    return number % 2 == 0, number

if __name__ == "__main__":
    with Pool(processes=2) as executor:
        result, number = executor.apply(is_even, args=(10,))
        info(f'Is {number} even? {result}')
