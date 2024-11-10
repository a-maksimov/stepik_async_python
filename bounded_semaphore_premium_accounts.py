import asyncio


async def convert_file(filename, semaphore):
    async with semaphore:
        await asyncio.sleep(1)
        print(f"Файл {filename} обработан")


async def main():
    semaphores = {
        'free': asyncio.BoundedSemaphore(2),
        'premium': asyncio.BoundedSemaphore(10),
    }
    tasks = [convert_file(filename, semaphores[account]) for filename in files]
    await asyncio.gather(*tasks)


files = input().split()
account = input()
asyncio.run(main())
