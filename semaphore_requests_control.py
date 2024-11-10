import asyncio

semaphore = asyncio.Semaphore(3)
requests = 0

users = ["sasha", "petya", "masha", "katya", "dima", "olya", "igor", "sveta", "nikita", "lena",
         "vova", "yana", "kolya", "anya", "roma", "nastya", "artem", "vera", "misha", "liza"]


async def request(user):
    global requests
    async with semaphore:
        print(f'Пользователь {user} делает запрос')
        await asyncio.sleep(1)
        print(f'Запрос от пользователя {user} завершен')
        requests += 1
        print(f'Всего запросов: {requests}')


async def main():
    tasks = asyncio.gather(*[request(user) for user in users])
    await tasks

asyncio.run(main())
