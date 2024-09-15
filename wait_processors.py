import asyncio

# Полный словарь вшит в задачу

processors_delays = {
    'Intel Core i9-11900K': 7.01,
    'Intel Core i7-11700K': 4.32,
    'Intel Core i5-11600K': 8.59,
    'AMD Ryzen 9 5950X': 2.53,
}


async def simulate_processing(delay):
    await asyncio.sleep(delay)


async def main():
    tasks = [asyncio.create_task(simulate_processing(processors_delays[processor]), name=processor) for processor in processors_delays]
    complete, _ = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    task = next(iter(complete))
    print(f"Первый завершенный процесс: {task.get_name()}")


asyncio.run(main())