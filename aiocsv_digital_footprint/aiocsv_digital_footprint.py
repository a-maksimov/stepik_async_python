import asyncio
from datetime import datetime
import json
from pathlib import Path

import aiofiles
from aiocsv import AsyncDictWriter

semaphore = asyncio.BoundedSemaphore(100)

date_format = '%d.%m.%Y %H:%M:%S'


async def process_file(filepath):
    data = []
    async with semaphore:
        async with aiofiles.open(filepath, mode='r', encoding='utf-8') as f:
            read_data = await f.read()
            json_data = json.loads(read_data)
    for item in json_data:
        if item['HTTP-статус'] == 200:
            item["Время и дата"] = datetime.strptime(
                item["Время и дата"], "%Y-%m-%d %H:%M:%S"
            ).strftime(date_format)
            data.append(item)
    return data


async def main():
    base_directory = Path("logs")
    all_files = base_directory.rglob("*.json")

    tasks = []
    for file in all_files:
        tasks.append(process_file(file))

    results = await asyncio.gather(*tasks)
    global_results = [res for result in results for res in result]
    global_results.sort(
        key=lambda x: datetime.strptime(x["Время и дата"], date_format)
    )

    fieldnames = list(next(iter(global_results)).keys())

    async with aiofiles.open('result.csv', 'w', encoding='utf-8-sig', newline='') as r:
        writer = AsyncDictWriter(r, fieldnames=fieldnames, lineterminator="\n", delimiter=';')
        await writer.writeheader()
        for row in global_results:
            await writer.writerow(row)


if __name__ == "__main__":
    asyncio.run(main())
