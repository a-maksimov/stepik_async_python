import asyncio
import aiohttp
import sys

if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def fetch_status(url, session):
    async with session.get(url) as response:
        return response.status


async def main():
    connector = aiohttp.TCPConnector(limit=10)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for i in range(1, 1001):
            tasks.append(fetch_status(f'https://asyncio.ru/zadachi/5/{i}.html', session))

        results = await asyncio.gather(*tasks)

    print(sum(results))

if __name__ == "__main__":
    asyncio.run(main())
