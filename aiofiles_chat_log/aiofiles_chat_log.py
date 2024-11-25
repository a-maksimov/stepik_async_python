import asyncio
import re

import aiofiles


async def write_to_file(player_name, message, delay):
    await asyncio.sleep(delay)
    async with aiofiles.open('chat_log.txt', 'a', encoding='utf-8') as file:
        await file.write(f"{delay:.2f}: {player_name}: {message}\n")


async def main():
    pattern = r'\("([^"]+)", "([^"]+)", ([0-9]*\.?[0-9]+)\)'
    tasks = []
    async with aiofiles.open('dataset_1048335_13.txt', 'r', encoding='utf-8') as file:
        await file.readline()
        async for line in file:
            match = re.search(pattern, line)
            if not match:
                continue
            player_name = match.group(1)
            message = match.group(2)
            delay = float(match.group(3))
            tasks.append(write_to_file(player_name, message, delay))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())