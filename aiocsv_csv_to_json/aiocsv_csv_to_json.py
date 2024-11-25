import asyncio
import json

import aiofiles
from aiocsv import AsyncDictReader


async def main():
    data = []
    async with aiofiles.open('address_10000.csv', mode='r', encoding='utf-8-sig', newline="") as f:
        async for row in AsyncDictReader(f, delimiter=";"):
            data.append(row)

    async with aiofiles.open('result.json', 'a', encoding='utf-8') as r:
        json_data = json.dumps(data, indent=4, ensure_ascii=False)
        await r.write(json_data)


if __name__ == "__main__":
    asyncio.run(main())
