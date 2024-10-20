import asyncio
from asyncio import LifoQueue


async def autosave(queue):
    for time in range(1, 21):
        await asyncio.sleep(0.1)
        await queue.put(f"Автосохранение {time}")
        print(f"Автосохранение игры через {time} часов")


async def simulate_gameplay(queue):
    for time in range(1, 21):
        await asyncio.sleep(0.1)
        if time % 5 == 0:
            autosave = await queue.get()
            print(f"Загружена последняя версия игры: {autosave}")
            queue.task_done()


async def main():
    queue = LifoQueue()
    await asyncio.gather(autosave(queue), simulate_gameplay(queue))

    print('Игра пройдена!')

asyncio.run(main())
