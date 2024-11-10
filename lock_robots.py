import asyncio

lock = asyncio.Lock()
counter = 0


async def robot_task(robot_id):
    name = asyncio.current_task().get_name()
    global counter
    async with lock:
        temp = counter
        print(f"Робот {name}({robot_id}) передвигается к месту A")
        await asyncio.sleep(0.1)
        counter = temp + 1
        print(f"Робот {name}({robot_id}) достиг места A. Место A посещено {counter} раз")


async def main():
    robot_names = ['Электра', 'Механикс', 'Оптимус', 'Симулакр', 'Футуриус']
    tasks = [asyncio.create_task(robot_task(robot_id), name=robot) for robot_id, robot in enumerate(robot_names)]
    await asyncio.gather(*tasks)


asyncio.run(main())
