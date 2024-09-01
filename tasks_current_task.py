import asyncio


async def process_task():
    await asyncio.sleep(1)
    return id(asyncio.current_task())


async def main():
    tasks = [process_task() for _ in range(10)]
    result = await asyncio.gather(*tasks)
    return result


asyncio.run(main())
