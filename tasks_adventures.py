import asyncio


async def countdown(name, seconds):
    for i in range(seconds):
        remains = seconds - i
        if name == "Квест на поиск сокровищ":
            print(f"{name}: Осталось {remains} сек. Найди скрытые сокровища!")
        else:
            print(f"{name}: Осталось {remains} сек. Беги быстрее, дракон на хвосте!")
        await asyncio.sleep(1)

    print(f"{name}: Задание выполнено! Что дальше?")


async def main():
    treasure_hunt = asyncio.create_task(countdown("Квест на поиск сокровищ", 10))
    dragon_escape = asyncio.create_task(countdown("Побег от дракона", 5))
    await asyncio.gather(treasure_hunt, dragon_escape)


asyncio.run(main())
