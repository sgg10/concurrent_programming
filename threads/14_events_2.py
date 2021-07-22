from logging_utils import info, THREAD_FORMAT
import logging
import threading
import requests

logging.basicConfig(level=logging.DEBUG, format=THREAD_FORMAT)

user = dict()

def generate_request(url:str, event: threading.Event) -> None:
    global user
    response = requests.get(url)

    if response.status_code == 200:
        response_json = response.json()

        user = response_json.get("results")[0]
        event.set()

def show_user_name(event: threading.Event) -> None:
    event.wait()
    name = user.get("name").get("first")
    info(f"User name is: {name}")

if __name__ == "__main__":
    event = threading.Event()
    thread1 = threading.Thread(target=generate_request, args=("https://randomuser.me/api", event))
    thread2 = threading.Thread(target=show_user_name, args=(event,))

    thread1.start()
    thread2.start()
