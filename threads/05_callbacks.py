from logging_utils import info, error
import logging
import requests
import threading
from random import randint

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def get_pokemon_name(response_json):
    name = response_json.get("forms")[0].get("name")
    info(f"Pokemon name is: {name}")

def get_name_random(response_json):
    name = response_json.get("results")[0].get("name").get("first")
    info(f"User name is: {name}")

def error_response():
    error("Cannot complete the operation")

def generate_request(url, success_callback, error_callback):
    response = requests.get(url)

    if response.status_code == 200:
        success_callback(response.json())
    else:
        error_callback()

if __name__ == "__main__":
    thread1 = threading.Thread(target=generate_request, kwargs={
        'url': f'https://pokeapi.co/api/v2/pokemon/{randint(1, 151)}/',
        'success_callback': get_pokemon_name,
        'error_callback': error_response
    })
    thread2 = threading.Thread(target=generate_request, kwargs={
        'url': 'https://randomuser.me/api/',
        'success_callback': get_name_random,
        'error_callback': error_response
    })
    thread1.start()
    thread2.start()