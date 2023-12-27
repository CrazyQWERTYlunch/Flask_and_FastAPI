import os
import time
import threading
from pathlib import Path
import requests


BASE_DIR = os.path.join(Path(__file__).resolve().parent, 'saves')

if not os.path.exists(BASE_DIR):
    os.mkdir(BASE_DIR)

urls = [
    'https://ya.ru',
    'https://google.com',
    'https://www.youtube.com',
    'https://www.rambler.ru',
    'https://gb.ru',
    'https://mail.ru',
    'https://www.python.org/',
]


def download_content(url: str):
    response = requests.get(url)
    filename = (
        url.replace('https://', '').replace('.', '_').replace('/', '-')
        + '_thread.html'
    )
    with open(os.path.join(BASE_DIR, filename), 'w', encoding='utf-8') as f:
        f.write(response.text)


threads: list[threading.Thread] = []


start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download_content, args=[url])
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print(f'Completed download in {time.time() - start_time} seconds.')