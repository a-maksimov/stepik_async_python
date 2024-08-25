import asyncio


async def coroutine_1():
    await asyncio.sleep(0.1)  # Задержка для первого сообщения
    print("Сообщение 1 от корутины 1")
    await asyncio.sleep(0.7)  # Задержка для второго сообщения
    print("Сообщение 2 от корутины 1")


async def coroutine_2():
    await asyncio.sleep(0.2)
    print("Сообщение 1 от корутины 2")
    await asyncio.sleep(0.8)
    print("Сообщение 2 от корутины 2")


async def coroutine_3():
    await asyncio.sleep(0.3)
    print("Сообщение 1 от корутины 3")
    await asyncio.sleep(0.9)
    print("Сообщение 2 от корутины 3")


async def coroutine_4():
    await asyncio.sleep(0.4)
    print("Сообщение 1 от корутины 4")
    await asyncio.sleep(1.0)
    print("Сообщение 2 от корутины 4")


async def coroutine_5():
    await asyncio.sleep(0.5)
    print("Сообщение 1 от корутины 5")
    await asyncio.sleep(1.2)
    print("Сообщение 2 от корутины 5")


async def coroutine_6():
    await asyncio.sleep(0.6)
    print("Сообщение 1 от корутины 6")
    await asyncio.sleep(1.3)
    print("Сообщение 2 от корутины 6")


async def main():
    await asyncio.gather(
        coroutine_1(),
        coroutine_2(),
        coroutine_3(),
        coroutine_4(),
        coroutine_5(),
        coroutine_6(),
    )


asyncio.run(main())


# Сообщение 1 от корутины 1
# Сообщение 1 от корутины 2
# Сообщение 1 от корутины 3
# Сообщение 1 от корутины 4
# Сообщение 1 от корутины 5
# Сообщение 1 от корутины 6
# Сообщение 2 от корутины 1
# Сообщение 2 от корутины 2
# Сообщение 2 от корутины 3
# Сообщение 2 от корутины 4
# Сообщение 2 от корутины 5
# Сообщение 2 от корутины 6
