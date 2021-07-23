from typing import Optional
from logging_utils import info, PROCESS_FORMAT
import logging
import multiprocessing
from time import sleep
from multiprocessing.connection import Connection

logging.basicConfig(level=logging.DEBUG, format=PROCESS_FORMAT)

# PIPES

class Publisher(multiprocessing.Process):
    def __init__(self, connection: Connection, name: Optional[str]=None, daemon: Optional[bool]=False) -> None:
        self.connection = connection
        multiprocessing.Process.__init__(self, name=name, daemon=daemon)

    def run(self) -> None:
        info("We are in Publisher process")
        for x in range(20):
            self.connection.send(f"Hi, from publisher process, with value {x}")
        self.connection.send(None)
        self.connection.close()


class Subscriber(multiprocessing.Process):
    def __init__(self, connection: Connection, name: Optional[str]=None, daemon: Optional[bool]=False) -> None:
        self.connection = connection
        self.is_alive = True
        multiprocessing.Process.__init__(self, name=name, daemon=daemon)

    def run(self) -> None:
        info("We are in Subscriber process")
        while self.is_alive:
            result = self.connection.recv()

            self.is_alive = result is not None

            info(result)

            sleep(0.5)
        else:
            self.connection.close()



if __name__ == "__main__":
    connection1, connection2 = multiprocessing.Pipe()
    publisher = Publisher(connection=connection1)
    subscriber = Subscriber(connection=connection2)

    publisher.start()
    subscriber.start()