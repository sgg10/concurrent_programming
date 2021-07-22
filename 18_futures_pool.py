from typing import Iterable, Union
from logging_utils import info, THREAD_FORMAT
import logging
import threading
from time import sleep
from random import randint
import requests
from concurrent.futures import ThreadPoolExecutor, Future

logging.basicConfig(level=logging.DEBUG, format=THREAD_FORMAT)

URLS = [
    'https://codigofacilito.com/',
    'https://twitter.com/home/',
    'https://www.google.com/',
    'https://es.stackoverflow.com/',
    'https://stackoverflow.com/',
    'https://about.gitlab.com/',
    'https://github.com/',
    'https://www.youtube.com/',
]

def check_status_callback(result: Iterable[Union[requests.Response, str]]) -> None:
    info(f"Server {result[1]} response is: {result[0].status_code}")

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [ executor.submit(lambda url: (requests.get(url), url), url) for  url in URLS ]
        for future in futures:
            future.add_done_callback(
                lambda future: check_status_callback(future.result())
            )