import os
import multiprocessing
from pathlib import Path
import time
import requests

BASE_DIR = Path(__file__).resolve().parent
saves_dir = os.path.join(BASE_DIR, 'saves')

if not os.path.exists(saves_dir):
    os.mkdir(saves_dir)

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
            + '_proc.html'
    )
    with open(os.path.join(saves_dir, filename), 'w', encoding='utf-8') as f:
        f.write(response.text)


processes = []

if __name__ == '__main__':
    start_time = time.time()

    for url in urls:
        process = multiprocessing.Process(target=download_content, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Completed download in {time.time() - start_time} seconds.')
