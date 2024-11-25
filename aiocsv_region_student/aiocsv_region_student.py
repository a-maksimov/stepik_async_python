import asyncio
import glob
import json

import aiofiles
from aiocsv import AsyncDictReader
semaphore = asyncio.BoundedSemaphore(100)


async def process_file(filepath):
    data = []
    async with semaphore:
        async with aiofiles.open(filepath, mode='r', encoding='utf-8-sig', newline="") as f:
            async for row in AsyncDictReader(f, delimiter=","):
                if float(row['Балл ЕГЭ']) == 100:
                    data.append(row)

    return data


async def main():
    tasks = []
    for file in glob.glob('Задача Студенты/**/*.csv'):
        tasks.append(process_file(file))

    results = await asyncio.gather(*tasks)

    students = sorted([r for result in results for r in result], key=lambda x: x['Телефон для связи'])

    async with aiofiles.open('result.json', 'w', encoding='utf-8') as r:
        json_data = json.dumps(students, indent=4, ensure_ascii=False)
        await r.write(json_data)

if __name__ == "__main__":
    asyncio.run(main())
