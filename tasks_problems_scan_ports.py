import asyncio
import random


async def scan_range(address, range_ports):
    print(f"Сканирование портов с {range_ports[0]} по {range_ports[-1]} на адресе {address}")
    tasks = [scan_port(address, port) for port in range_ports]
    results = await asyncio.gather(*tasks)
    return results


async def scan_port(address, port):
    await asyncio.sleep(1)
    result = random.randint(0, 1)
    if result:
        print(f"Порт {port} на адресе {address} открыт")
        return port


async def main():
    address = "192.168.0.1"
    port_range = range(80, 86)
    task = asyncio.create_task(scan_range(address, list(port_range)))
    results = await task
    open_ports = [port for port in results if port]
    if open_ports:
        print(f"Открытые порты на адресе {address}: {open_ports}")
    else:
        print(f"Открытых портов на адресе {address} не найдено")


asyncio.run(main())
