import asyncio


async def generate(num):
    print(f"Корутина generate с аргументом {num}")


async def main():
    for num in range(10):
        await generate(num)


asyncio.run(main())
