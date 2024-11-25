import asyncio
import os
import aiofiles

even_sum = 0
semaphore = asyncio.Semaphore(10)


async def add_number(filename):
    global even_sum
    folder = 'files'
    filepath = f'{folder}\\{filename}'
    async with semaphore:
        async with aiofiles.open(filepath, mode='r', encoding='utf-8') as f:
            async for line in f:
                if float(line) % 2 == 0:
                    even_sum += float(line)


async def main():
    tasks = []
    for file in os.listdir("files"):
        tasks.append(add_number(file))

    await asyncio.gather(*tasks)
    print(even_sum)


if __name__ == "__main__":
    asyncio.run(main())
