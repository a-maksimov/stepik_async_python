import asyncio


async def activate_portal(x=2):
    print(f'Активация портала в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 2


async def perform_teleportation(x):
    print(f'Телепортация в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x + 2


async def portal_operator():
    activate_future = asyncio.ensure_future(activate_portal())
    result_activate = await activate_future
    if result_activate > 4:
        teleport_future = asyncio.ensure_future(perform_teleportation(1))
    else:
        teleport_future = asyncio.ensure_future(perform_teleportation(result_activate))
    result_teleport = await teleport_future
    print(f'Результат активации портала: {result_activate} единиц энергии')
    print(f'Результат телепортации: {result_teleport} единиц времени')


async def main():
    future = asyncio.ensure_future(portal_operator())
    await future


asyncio.run(main())
