import asyncio


async def coro(num):
    await asyncio.sleep(num * 0.1)
    print(f'Задача {num} выполнена')


async def main():
    for i in range(5):
        asyncio.create_task(coro(i))
    tasks = asyncio.all_tasks()
    await asyncio.gather(*[task for task in tasks if task.get_name() != 'Task-1'])
    print('Работа программы завершена')


asyncio.run(main())