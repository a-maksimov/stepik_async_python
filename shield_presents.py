import asyncio

# Время доставки до разных городов:
delivery_times = {
    'Москва': 1,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 4,
    'Челябинск': 6,
    'Омск': 7,
    'Красноярск': 8,
    'Владивосток': 9,
    'Хабаровск': 9
}

# Заказы:
orders = [('Новогодняя кружка', 'Москва', 'нет'),
          ('Шоколадный набор', 'Красноярск', 'нет'),
          ('Ручка и блокнот', 'Новосибирск', 'важно'),
          ('Носки с новогодним принтом', 'Владивосток', 'нет')]

# Время до нового года:
days_left = 3


# Тут пишите ваш код:
async def deliver(order):
    await asyncio.sleep(delivery_times[order[1]])
    print(f'Подарок {order[0]} успешно доставлен в г. {order[1]}')


async def main():
    tasks = []
    important_tasks = []
    for order in orders:
        task = asyncio.create_task(deliver(order))
        if order[2] == 'важно':
            important_tasks.append(task)
            tasks.append(asyncio.shield(task))
            continue
        tasks.append(task)

    done, pending = await asyncio.wait(tasks, timeout=days_left)
    [pending_task.cancel() for pending_task in pending]

    # Дожидаемся завершения всех задач.
    for task in important_tasks:
        await task


asyncio.run(main())
