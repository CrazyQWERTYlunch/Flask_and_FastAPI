import time
import threading
from random import randint


def get_sum(lst: list[int]):
    global total_sum
    lst_sum = 0

    for el in lst:
        lst_sum += el

    total_sum += lst_sum


total_sum: int = 0
main_list: list[int] = []
threads: list[threading.Thread] = []
start_time = time.time()


for _ in range(1000):
    # new_list = [1 for _ in range(1000)]
    new_list = [randint(1, 100) for _ in range(1000)]
    thread = threading.Thread(target=get_sum, args=[new_list])
    main_list.extend(new_list)
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()


print(main_list)
print(f'{total_sum = }')
print(f'Потребовалось {time.time() - start_time} секунд!')