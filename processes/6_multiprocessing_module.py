from logging_utils import info, PROCESS_FORMAT
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format=PROCESS_FORMAT)

if __name__ == "__main__":
    current_process = multiprocessing.current_process()
    pid = current_process.pid
    name = current_process.name

    info(f"Current process is: {current_process}")
    info(f"Id of process is: {pid}")
    info(f"name of process is: {name}")