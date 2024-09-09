import asyncio


async def activate_portal(x=2):
    print(f'Активация портала в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 2


async def perform_teleportation(x=3):
    print(f'Телепортация в процессе, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x + 2


async def recharge_portal(x=4):
    print(f'Подзарядка портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 3


async def check_portal_stability(x=5):
    print(f'Проверка стабильности портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x + 4


async def restore_portal(x=6):
    print(f'Восстановление портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x * 5


async def close_portal(x=7):
    print(f'Закрытие портала, требуется времени: {x} единиц')
    await asyncio.sleep(x)
    return x - 1


async def portal_operator():
    activate_portal_task = asyncio.create_task(activate_portal())
    perform_teleportation_task = asyncio.create_task(perform_teleportation())
    recharge_portal_task = asyncio.create_task(recharge_portal())
    check_portal_stability_task = asyncio.create_task(check_portal_stability())
    restore_portal_task = asyncio.create_task(restore_portal())
    close_portal_task = asyncio.create_task(close_portal())

    tasks = [
        activate_portal_task,
        perform_teleportation_task,
        recharge_portal_task,
        check_portal_stability_task,
        restore_portal_task,
        close_portal_task
    ]
    await asyncio.gather(*tasks)

    print(f'Результат активации портала: {activate_portal_task.result()} единиц энергии')
    print(f'Результат телепортации: {perform_teleportation_task.result()} единиц времени')
    print(f'Результат подзарядки портала: {recharge_portal_task.result()} единиц энергии')
    print(f'Результат проверки стабильности: {check_portal_stability_task.result()} единиц времени')
    print(f'Результат восстановления портала: {restore_portal_task.result()} единиц энергии')
    print(f'Результат закрытия портала: {close_portal_task.result()} единиц времени')


async def main():
    future = asyncio.ensure_future(portal_operator())
    await future


asyncio.run(main())
