import os
import aiohttp
import asyncio
import aiofiles
from pathlib import Path
import time

task_dir = os.path.join(Path(__file__).resolve().parent, 'task_9')

if not os.path.exists(task_dir):
    os.mkdir(task_dir)

BASE_DIR = os.path.join(task_dir, 'async')

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


async def download_image(url: str):
    global start_time
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            paths = url.replace('https://', '').split('/')
            dirname, filename = paths[0].replace('.', '_'), paths[-1]
            if not os.path.exists(os.path.join(BASE_DIR, dirname)):
                os.mkdir(os.path.join(BASE_DIR, dirname))

            async with aiofiles.open(
                    os.path.join(BASE_DIR, dirname, filename), 'wb'
            ) as f:
                await f.write(await response.content.read())
            print(f'{time.time() - start_time} на картинку')

async def main():
    tasks = []

    for url in urls:
        task = asyncio.ensure_future(download_image(url))
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    print(f'Completed download in {time.time() - start_time} seconds.')
