import asyncio

max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}

counters = {
    "Counter 1": 0,
    "Counter 2": 0,
    "Counter 3": 0
}

delays = {
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}


async def counter(counter_name, delay):
    for i in range(max_counts[counter_name]):
        counters[counter_name] += 1
        await asyncio.sleep(delay)
        print(f'{counter_name}: {counters[counter_name]}')


async def main():
    tasks = [asyncio.create_task(counter(name, delays[name])) for name in counters]
    await asyncio.gather(*tasks)

asyncio.run(main())
