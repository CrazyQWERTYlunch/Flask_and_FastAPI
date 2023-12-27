import time
import multiprocessing
from random import randint


def get_sum(lst: list[int], cnt: multiprocessing.Value):
    lst_sum = 0

    for el in lst:
        lst_sum += el

    with cnt.get_lock():
        cnt.value += lst_sum


def main():
    total_sum = multiprocessing.Value('i', 0)
    main_list: list[int] = []
    processes: list[multiprocessing.Process] = []

    for _ in range(1000):
        # new_list = [1 for _ in range(1000)]
        new_list = [randint(1, 100) for _ in range(1000)]
        process = multiprocessing.Process(
            target=get_sum, args=(new_list, total_sum)
        )
        main_list.extend(new_list)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(main_list)

    return total_sum


if __name__ == '__main__':
    start_time = time.time()
    res = main()

    with res.get_lock():
        total_sum = res.value

    print(f'{total_sum = }')
    print(f'Потребовалось {time.time() - start_time} секунд!')