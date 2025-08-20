# https://stackoverflow.com/questions/50757497/simplest-async-await-example-possible-in-python
# Case 1: just normal Python

import time

def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)


def sum_(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')


if __name__ == "__main__":
    start = time.time()
    tasks = [
        sum_("A", [1, 2]),
        sum_("B", [1, 2, 3]),
    ]
    end = time.time()

    print(f'Time: {end - start:.2f} sec')
