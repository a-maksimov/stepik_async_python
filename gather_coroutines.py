import asyncio


async def coroutine_1():
    print('Coroutine 1 is done')


async def coroutine_2():
    print('Coroutine 2 is done')


async def coroutine_3():
    print('Coroutine 3 is done')


async def main():
    tasks = [
        asyncio.create_task(coroutine)
        for coroutine
        in [coroutine_1, coroutine_2, coroutine_3]
    ]
    await asyncio.gather(tasks)


asyncio.run(main())
