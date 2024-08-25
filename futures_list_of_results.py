import asyncio


async def main():
    awaitables = [aw for aw in await get_coros_and_tasks()]
    tasks = [asyncio.ensure_future(aw) for aw in awaitables]
    await asyncio.gather(*tasks)
    return [task.result() for task in tasks]





