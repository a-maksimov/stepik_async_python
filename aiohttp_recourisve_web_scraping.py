import asyncio
import aiohttp
import sys
from bs4 import BeautifulSoup

number = 0

if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def process_link(base_url, session):
    global number
    async with session.get(base_url) as response:
        html_content = await response.text()
        # Создаём объект супа для простого извлечения тега
        soup = BeautifulSoup(html_content, 'html.parser')

        # Извлекаем числа из тега
        p_tags = soup.find('p', id='number')
        if p_tags:
            number += float(p_tags.text)

        # Находим все ссылки на странице
        links = soup.find_all('a', {'class': 'link'})
        extracted_urls = [link['href'] for link in links if 'href' in link.attrs]
        updated_urls = [
            f"{base_url.rsplit('/', 1)[0]}/{url}" for url in extracted_urls
        ]
        tasks = []
        for link in updated_urls:
            tasks.append(process_link(link, session))
        await asyncio.gather(*tasks)


async def main():
    url = f"https://asyncio.ru/zadachi/3/index.html"

    connector = aiohttp.TCPConnector(limit=75)
    async with aiohttp.ClientSession(connector=connector) as session:
        task = asyncio.create_task(process_link(url, session))
        await task
    print(number)


if __name__ == "__main__":
    asyncio.run(main())
