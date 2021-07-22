from logging_utils import info, debug, ONLY_MESSAGE_FORMAT
import logging
import threading
import requests
from random import randint
from concurrent.futures import Future

logging.basicConfig(level=logging.DEBUG, format=ONLY_MESSAGE_FORMAT)

def show_pokemon_name(response):
    if response.status_code == 200:
        response_json = response.json()
        name = response_json.get("forms")[0].get("name")
        info(f"Pokemon name is: {name}")

def generate_request(url):
    future = Future()

    thread = threading.Thread(target=(
        lambda: future.set_result(requests.get(url))
    ))

    thread.start()

    return future

if __name__ == "__main__":
    future = generate_request(f"https://pokeapi.co/api/v2/pokemon/{randint(0, 151)}/")
    future.add_done_callback(
        lambda future: show_pokemon_name(future.result())
    )

    while not future.done():
        debug("Waiting for result...")
    else:
        debug("Script ended")