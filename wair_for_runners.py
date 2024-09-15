import asyncio

# Словарь бегунов: Имя + скорость бега (м/с)
# Полный список бегунов скрыт под капотом задачи.
runners = {
    "Молния Марк": 12.8,
    "Ветреный Виктор": 13.5,
    "Скоростной Степан": 11.2,
    "Быстрая Белла": 10.8,

}

DISTANCE = 100
MAX_TIME = 10


async def run_lap(name, speed):
    time_needed = round(DISTANCE / speed, 2)
    await asyncio.sleep(time_needed)
    print(f"{name} завершил круг за {time_needed} секунд")


async def main():
    tasks = [run_lap(name, speed) for name, speed in runners.items()]
    try:
        await asyncio.wait_for(asyncio.gather(*tasks), MAX_TIME)
    except TimeoutError:
        pass


asyncio.run(main())
