import asyncio

import aiofiles
import aiohttp
import sys
from bs4 import BeautifulSoup
import os

if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def download_image(img_url, folder, session):
    try:
        async with session.get(img_url) as response:
            if response.status == 200:
                img_data = await response.read()
                # Extract the image filename
                img_name = os.path.basename(img_url)
                # Define the file path
                file_path = os.path.join(folder, img_name)
                # Save the image
                async with aiofiles.open(file_path, 'wb') as img_file:
                    await img_file.write(img_data)
                print(f"Downloaded: {img_url} -> {file_path}")
    except Exception as e:
        print(f"Failed to download {img_url}: {e}")


async def process_link(base_url, session, download_folder):
    async with session.get(base_url) as response:
        html_content = await response.text()
        # Создаём объект супа для простого извлечения тега
        soup = BeautifulSoup(html_content, 'html.parser')
        main_tag = soup.find('main')
        img_tags = main_tag.find_all('img')

        # Extract and download all images
        tasks = []
        for img_tag in img_tags:
            img_src = img_tag.get('src')
            if img_src:
                # Handle relative URLs
                img_url = img_src if img_src.startswith('http') else f"{base_url.rsplit('/', 1)[0]}/{img_src}"
                tasks.append(download_image(img_url, download_folder, session))

        await asyncio.gather(*tasks)


async def main():
    url = f"https://asyncio.ru/zadachi/4/index.html"

    connector = aiohttp.TCPConnector(limit=75)
    async with aiohttp.ClientSession(connector=connector) as session:
        task = asyncio.create_task(process_link(url, session, r"downloaded_images"))
        await task


def get_folder_size(folder_path):
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size


if __name__ == "__main__":
    asyncio.run(main())
    folder_path = r"downloaded_images"
    print(get_folder_size(folder_path))
