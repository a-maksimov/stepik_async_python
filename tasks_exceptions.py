import asyncio


async def main():
    task = asyncio.create_task(coroutine())
    try:
        await task
    except Exception as e:
        print(e)


asyncio.run(main())
