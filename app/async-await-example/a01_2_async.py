# https://stackoverflow.com/questions/50757497/simplest-async-await-example-possible-in-python
# Case 2: async/await done wrong

import asyncio
import time


async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)


async def sum_(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')


if __name__ == "__main__":
    start = time.time()

    loop = asyncio.new_event_loop()
    tasks = [
        loop.create_task(sum_("A", [1, 2])),
        loop.create_task(sum_("B", [1, 2, 3])),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

    end = time.time()
    print(f'Time: {end - start:.2f} sec')
