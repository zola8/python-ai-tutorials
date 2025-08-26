# https://docs.python.org/3/library/asyncio-task.html

import asyncio


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


if __name__ == '__main__':
    # main()
    # RuntimeWarning: coroutine 'main' was never awaited
    asyncio.run(main())
