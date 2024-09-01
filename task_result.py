import asyncio


async def main():
    task = asyncio.create_task(coroutine())
    await task
    print(task.result())


asyncio.run(main())
