import asyncio


async def coro_1(func):
    print(f'{coro_1.__name__} says, hello {func.__name__}!')


async def coro_2(func):
    print(f'{coro_2.__name__} says, hello {func.__name__}!')


async def main():
    await coro_1(coro_2)
    await coro_2(coro_1)


asyncio.run(main())
