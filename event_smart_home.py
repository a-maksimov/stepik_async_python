import asyncio

ip = ["192.168.0.3", "192.168.0.1", "192.168.0.2", "192.168.0.4", "192.168.0.5"]

event = asyncio.Event()


async def sensor(i, address):
    print(f'Датчик {i} IP-адрес {address} настроен и ожидает срабатывания')
    await event.wait()
    print(f'Датчик {i} IP-адрес {address} активирован, "Wee-wee-wee-wee"')


async def alarm():
    await asyncio.sleep(5)
    event.set()
    print('Датчики зафиксировали движение')


async def main():
    tasks = [sensor(i, address) for i, address in enumerate(ip)] + [asyncio.create_task(alarm())]
    await asyncio.gather(*tasks)


asyncio.run(main())
