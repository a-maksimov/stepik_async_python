import asyncio

storage = 0

wood_resources_dict = {
    'Деревянный меч': 6,
    'Деревянный щит': 12,
    'Деревянный стул': 24,
}


async def gather_wood(event, condition):
    global storage
    while True:
        async with condition:
            if event.is_set():
                break
            await asyncio.sleep(1)
            storage += 2
            print(f"Добыто 2 ед. дерева. На складе {storage} ед.")
            condition.notify_all()


async def craft_item(event, condition):
    global storage
    for item, wood in wood_resources_dict.items():
        async with condition:
            while storage < wood:
                await condition.wait()
            storage -= wood
            print(f"Изготовлен {item}.")
    event.set()


async def main():
    condition = asyncio.Condition()
    event = asyncio.Event()
    gather_task = asyncio.create_task(gather_wood(event, condition))
    craft_task = asyncio.create_task(craft_item(event, condition))
    await asyncio.gather(gather_task, craft_task)


if __name__ == "__main__":
    asyncio.run(main())
