import asyncio

# Каждое значение словаря, это необходимое количество ресурса для изготовления предмета
stone_resources_dict = {
    'Каменная плитка': 10,
    'Каменная ваза': 40,
    'Каменный столб': 50,
}

metal_resources_dict = {
    'Металлическая цепь': 6,
    'Металлическая рамка': 24,
    'Металлическая ручка': 54,
}

cloth_resources_dict = {
    'Тканевая занавеска': 8,
    'Тканевый чехол': 24,
    'Тканевое покрывало': 48,
}

resources = [0, 0, 0]


async def gather(resource_name, value, event, condition, index):
    global resources
    while not event.is_set():
        async with condition:
            await asyncio.sleep(1)
            if event.is_set():
                break
            resources[index] += value
            print(f"Добыто {value} ед. {resource_name}. На складе {resources[index]} ед.")
            condition.notify_all()
            await asyncio.sleep(0)


async def craft_item(resource_dict, resource_name, event, condition, index):
    global resources
    for item, value in resource_dict.items():
        async with condition:
            while resources[index] < value:
                await condition.wait()
            resources[index] -= value
            print(f"Изготовлен {item} из {resource_name}.")
            # Завершаем работу, как только изготовлен последний предмет
            if item == list(resource_dict.keys())[-1]:
                event.set()


async def main():
    gather_tasks = []
    craft_tasks = []
    task_dict = {
        'камня': stone_resources_dict,
        'металла': metal_resources_dict,
        'ткани': cloth_resources_dict
    }
    value_dict = {
        'камня': 10,
        'металла': 6,
        'ткани': 8
    }
    for i, resource_name in enumerate(['камня', 'металла', 'ткани']):
        condition = asyncio.Condition()
        event = asyncio.Event()
        gather_task = asyncio.create_task(gather(resource_name, value_dict[resource_name], event, condition, i))
        gather_tasks.append(gather_task)
        craft_task = asyncio.create_task(craft_item(task_dict[resource_name], resource_name, event, condition, i))
        craft_tasks.append(craft_task)
    await asyncio.gather(*gather_tasks, *craft_tasks)


asyncio.run(main())