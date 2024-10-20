import asyncio
import random

random.seed(1)

SERVERS = [
    "api.database.local",
    "auth.backend.local",
    "web.frontend.local",
    "cache.redis.local",
    "analytics.bigdata.local"
]

STATUSES = ["Online", "Offline", "Maintenance", "Error"]


async def monitor_servers(servers):
    for server in servers:
        await asyncio.sleep(0.1)
        status = random.choice(STATUSES)
        yield server, status


async def main():
    async for server, status in monitor_servers(SERVERS):
        print(f'{server}: состояние {status}')


asyncio.run(main())
