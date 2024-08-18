import asyncio


async def print_hello():
    print('Hello, Asyncio!')


async def main():
    await print_hello()


asyncio.run(main())
