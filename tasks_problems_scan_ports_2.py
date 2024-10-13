import asyncio
import random

ip_dct = {'192.168.0.1': [0, 100], '192.168.0.2': [225, 300], '192.168.2.5': [150, 185]}


async def scan_range(address, start_port, end_port):
    print(f"Scanning ports {start_port}-{end_port} on {address}")
    tasks = [scan_port(address, port) for port in range(start_port, end_port + 1)]
    results = await asyncio.gather(*tasks)
    return address, [port for port in results if port is not None]


async def scan_port(address, port):
    """
    Асинхронная функция, имитирующая сканирование порта на заданном ip-адресе.
    """
    await asyncio.sleep(1)
    if random.randint(0, 100) == 1:
        print(f"Port {port} on {address} is open")
        return port


async def main(ip_dct):
    tasks = [scan_range(address, range_ports[0], range_ports[-1]) for address, range_ports in ip_dct.items()]
    results = await asyncio.gather(*tasks)
    for result in results:
        if not result[1]:
            continue
        print(f"Всего найдено открытых портов {len(result[1])} {result[1]} для ip: {result[0]}")

asyncio.run(main(ip_dct))
