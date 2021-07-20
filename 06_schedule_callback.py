from logging_utils import info, error
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

# Timer
def callback():
    info("Hi, I'm a callback that does not execute immediately")


if __name__ == "__main__":
    thread = threading.Timer(3, callback)
    thread.start()

    info("Hi, I'm a main thread")