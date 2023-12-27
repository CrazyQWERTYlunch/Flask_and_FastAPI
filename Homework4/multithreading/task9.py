import os
import time
import threading
from pathlib import Path
import requests


task_dir = os.path.join(Path(__file__).resolve().parent, 'task_9')

if not os.path.exists(task_dir):
    os.mkdir(task_dir)

BASE_DIR = os.path.join(task_dir, 'threads')

if not os.path.exists(BASE_DIR):
    os.mkdir(BASE_DIR)

urls = [
    'https://funik.ru/wp-content/uploads/2018/10/17478da42271207e1d86.jpg',
    'https://images.wallpaperscraft.ru/image/single/gorod_vid_sverhu_doroga_156925_1280x720.jpg',
    'https://images.wallpaperscraft.ru/image/single/ulitsa_luzha_otrazhenie_139688_1280x720.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/0/0c/Arithmetria.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Writing_table_%28bureau_plat%29_MET_DP105403.jpg/330px-Writing_table_%28bureau_plat%29_MET_DP105403.jpg',
    'https://roliki-magazin.ru/wp-content/uploads/2/9/f/29fa8fbd8ef15d5e168aa3143e282c51.jpeg'
]


def download_image(url: str):
    response = requests.get(url)
    paths = url.replace('https://', '').split('/')
    dirname, filename = paths[0].replace('.', '_'), paths[-1]

    if not os.path.exists(os.path.join(BASE_DIR, dirname)):
        os.mkdir(os.path.join(BASE_DIR, dirname))

    with open(os.path.join(BASE_DIR, dirname, filename), 'wb') as f:
        f.write(response.content)


threads: list[threading.Thread] = []

start_time = time.time()

for url in urls:
    thread = threading.Thread(target=download_image, args=[url])
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
    print(f'{time.time() - start_time} на картинку')

print(f'Completed download in {time.time() - start_time} seconds.')