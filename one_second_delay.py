import asyncio


async def print_with_delay(delay, func=None):
    if func is None:
        await asyncio.sleep(1)
    else:
        await func
    print(f'Coroutine {delay} is done')


async def main():
    tasks = [asyncio.create_task(print_with_delay(0))]
    previous_task = tasks[0]
    for i in range(1, 10):
        tasks.append(asyncio.create_task(print_with_delay(i, previous_task)))
        previous_task = tasks[-1]
    await asyncio.gather(*tasks)

asyncio.run(main())