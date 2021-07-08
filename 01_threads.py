import requests
import threading

def get_name():
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        result = response.json().get('results')
        name = result[0].get('name').get('first')
        print(name)

if __name__ == "__main__":
    # Concurrent
    for _ in range(5):
        # get_name()
        thread = threading.Thread(target=get_name)
        thread.start()