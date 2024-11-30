import asyncio
import aiohttp
import sys
from bs4 import BeautifulSoup

if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

code_dict = {
    0: 'F',
    1: 'B',
    2: 'D',
    3: 'J',
    4: 'E',
    5: 'C',
    6: 'H',
    7: 'G',
    8: 'A',
    9: 'I'
}


async def fetch_page(url, session):
    async with session.get(url) as response:
        page_content = await response.text()
        soup = BeautifulSoup(page_content, 'html.parser')
        p_text = soup.find('p').text.strip()  # Удаление пробелов и переносов строки с обеих сторон строки
    for code, sym in code_dict.items():
        p_text = p_text.replace(str(code), sym)
    return p_text


async def main():
    connector = aiohttp.TCPConnector(limit=10)
    async with aiohttp.ClientSession(connector=connector) as session:
        task = asyncio.create_task(fetch_page(f'https://asyncio.ru/zadachi/1/index.html', session))
        result = await task
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
