import asyncio


async def main():
    awaitables = [aw for aw in await get_coros_and_tasks()]
    tasks = []
    for aw in awaitables:
        wrapped_aw = asyncio.ensure_future(aw)
        if aw is wrapped_aw:
            continue
        tasks.append(wrapped_aw)
    await asyncio.gather(*tasks)
    return [task.result() for task in tasks]