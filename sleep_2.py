import asyncio


async def coroutine_1(delay=0.1):
    print("Первое сообщение от корутины 1")
    await asyncio.sleep(delay * 3)  # Вторая задержка
    print("Второе сообщение от корутины 1")
    await asyncio.sleep(delay * 3)  # Первая задержка
    print("Третье сообщение от корутины 1")
    await asyncio.sleep(delay)  # Вторая задержка
    print("Четвертое сообщение от корутины 1")


async def coroutine_2(delay=0.1):
    print("Первое сообщение от корутины 2")
    await asyncio.sleep(delay * 2)  # Третья задержка
    print("Второе сообщение от корутины 2")
    await asyncio.sleep(delay * 2)  # Первая задержка
    print("Третье сообщение от корутины 2")
    await asyncio.sleep(delay * 5)  # Вторая задержка
    print("Четвертое сообщение от корутины 2")


async def coroutine_3(delay=0.1):
    print("Первое сообщение от корутины 3")
    await asyncio.sleep(delay)  # Третья задержка
    print("Второе сообщение от корутины 3")
    await asyncio.sleep(delay * 4)  # Первая задержка
    print("Третье сообщение от корутины 3")
    await asyncio.sleep(delay * 3)  # Вторая задержка
    print("Четвертое сообщение от корутины 3")


async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
    )


asyncio.run(main())

# Первое сообщение от корутины 1
# Первое сообщение от корутины 2
# Первое сообщение от корутины 3
# Второе сообщение от корутины 3
# Второе сообщение от корутины 2
# Второе сообщение от корутины 1
# Третье сообщение от корутины 2
# Третье сообщение от корутины 3
# Третье сообщение от корутины 1
# Четвертое сообщение от корутины 1
# Четвертое сообщение от корутины 3
# Четвертое сообщение от корутины 2
