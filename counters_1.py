import asyncio

max_counts = {
    "Counter 1": 13,
    "Counter 2": 7
}

counters = {
    "Counter 1": 0,
    "Counter 2": 0
}

delay = 1


async def counter(counter_name, delay):
    for i in range(max_counts[counter_name]):
        counters[counter_name] += 1
        await asyncio.sleep(delay)
        print(f'{counter_name}: {counters[counter_name]}')


async def main():
    tasks = [asyncio.create_task(counter(name, delay)) for name in counters]
    await asyncio.gather(*tasks)

asyncio.run(main())
