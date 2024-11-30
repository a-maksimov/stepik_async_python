import asyncio
import aiofiles
import aiohttp
import sys
from bs4 import BeautifulSoup


if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def fetch_number(url, session):
    async with session.get(url) as response:
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        p_tags = soup.find('p', id='number').text
    return float(p_tags)


async def main():
    urls = []
    async with aiofiles.open("problem_pages.txt", mode='r', encoding='utf-8') as f:
        async for line in f:
            url = f"https://asyncio.ru/zadachi/2/html/{line.strip()}.html"
            urls.append(url)

    connector = aiohttp.TCPConnector(limit=75)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for url in urls:
            tasks.append(fetch_number(url, session))

        results = await asyncio.gather(*tasks)

    print(sum(results))

if __name__ == "__main__":
    asyncio.run(main())
