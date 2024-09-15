# url_list = [...] вшит в задачу.
import asyncio


# Асинхронная функция, проверяющая валидность URL и скачивающая данные - ее писать не надо, она вшита в задачу!
# async def check_url(url):

# ваш код пишите тут:
async def main():
    [asyncio.create_task(check_url(url)) for url in url_list]
    await asyncio.sleep(1)
    print(len(asyncio.all_tasks()) - 1)


asyncio.run(main())