import asyncio
import glob
import aiofiles

sum = 0
semaphore = asyncio.Semaphore(100)


async def add_number(filepath):
    global sum
    async with semaphore:
        async with aiofiles.open(filepath, mode='r', encoding='utf-8', newline="") as f:
            async for row in f:
                sum += float(row)


async def main():
    tasks = []
    for file in glob.glob('5000folder/**/*.csv'):
        tasks.append(add_number(file))

    await asyncio.gather(*tasks)
    print(sum)


if __name__ == "__main__":
    asyncio.run(main())
