import os
import aiohttp
import asyncio
from pathlib import Path
import time


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


async def download_content(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = (
                url.replace('https://', '').replace('.', '_').replace('/', '-')
                + '_async.html'
            )
            with open(
                os.path.join(saves_dir, filename), 'w', encoding='utf-8'
            ) as f:
                f.write(await response.text())


async def main():
    tasks = []

    for url in urls:
        task = asyncio.ensure_future(download_content(url))
        tasks.append(task)

    await asyncio.gather(*tasks)



if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
    print(f'Completed download in {time.time()- start_time} seconds.')