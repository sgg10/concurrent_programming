from logging_utils import info, debug
import logging
import threading
from time import sleep

from concurrent.futures import Future

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

# Futures

def callback_future(future):
    debug("Hello, I am a callback that will not be executed until the future already has a value")
    info(f"Future is: {future.result()}", normal=True)

if __name__ == "__main__":
    future = Future()
    future.add_done_callback(callback_future)
    future.add_done_callback(
        lambda future: debug("Hi, I'm lambda")
    )

    info("We started a very complex task!")

    sleep(2)

    info("We finished a very complex task")

    future.set_result("SGG10")

    info("Future already has a value")