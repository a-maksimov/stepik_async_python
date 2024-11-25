import asyncio
import json
from pathlib import Path

import aiofiles
from aiocsv import AsyncDictReader
semaphore = asyncio.BoundedSemaphore(100)


async def process_file(filepath):
    result = {}
    async with semaphore:
        async with aiofiles.open(filepath, mode='r', encoding='cp1251', newline="") as f:
            async for row in AsyncDictReader(f, delimiter=";"):
                result[row['Состояние авто']] = result.get(row['Состояние авто'], 0) + float(row['Стоимость авто'])
    return result


async def main():
    base_directory = Path("auto")
    all_csv_files = base_directory.rglob("*.csv")

    tasks = []
    for file in all_csv_files:
        tasks.append(process_file(file))

    results = await asyncio.gather(*tasks)

    global_result = {}
    for result in results:
        for condition, total in result.items():
            global_result[condition] = global_result.get(condition, 0) + total

    async with aiofiles.open('result.json', 'w', encoding='utf-8') as r:
        json_data = json.dumps(global_result, indent=4, ensure_ascii=False)
        await r.write(json_data)

if __name__ == "__main__":
    asyncio.run(main())
