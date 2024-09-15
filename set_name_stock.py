# Товары на складе:
import asyncio

warehouse_store = {
    "Диван": 15,
    "Обеденный стол": 10,
}

# Заказ:
order = {'Диван': 5, 'Обеденный_стол': 3, 'Табуретка': 50, 'Гардероб': 1}


# Тут пишите ваш код:
async def check_store(item, quantity):
    if not warehouse_store.get(item):
        asyncio.current_task().set_name(f'Отсутствует: {item}')
    elif quantity > warehouse_store[item]:
        asyncio.current_task().set_name(f'Частично в наличии: {item}')
    else:
        asyncio.current_task().set_name(f'В наличии: {item}')


async def main():
    tasks = [asyncio.create_task(check_store(item, quantity)) for item, quantity in order.items()]
    await asyncio.gather(*tasks)
    for task in sorted(tasks, key=lambda t: t.get_name()):
        print(task.get_name())


asyncio.run(main())
