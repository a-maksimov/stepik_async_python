import asyncio

global_counter = 0

lock = asyncio.Lock()


async def increment():
    global global_counter
    async with lock:
        temp = global_counter
        await asyncio.sleep(.01)
        global_counter = temp + 2.39


async def main():
    await asyncio.gather(*[increment() for x in range(99)])


asyncio.run(main())
print(f"global_counter: {round(global_counter, 2)}")
