from typing import Iterable, Union
from logging_utils import info, THREAD_FORMAT
import logging
import threading
from time import sleep
from random import randint
import requests
from concurrent.futures import ThreadPoolExecutor, Future, as_completed

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

def check_status_code(response: requests.Response, url:str) -> None:
    info(f"Server {url} response is: {response.status_code}")

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [ executor.submit(lambda url: (requests.get(url), url), url) for  url in URLS ]
        for future in as_completed(futures):
            response, url = future.result()
            if response.status_code == 200:
                check_status_code(response, url)