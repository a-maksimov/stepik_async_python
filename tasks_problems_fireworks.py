import asyncio
import random
from itertools import product

shapes = ["circle", "star", "square", "diamond", "heart"]
colors = ["red", "blue", "green", "yellow", "purple"]
actions = ["change_color", "explode", "disappear"]


async def launch_firework(shape, color, action):
    print(f"Запущен {color} {shape} салют, в форме {action}!!!")
    await asyncio.sleep(random.randint(1, 5))
    print(f"Салют {color} {shape} завершил выступление {action}")


async def main():
    tasks = [launch_firework(shape, color, action) for shape, color, action in product(shapes, colors, actions)]
    await asyncio.gather(*tasks)

asyncio.run(main())
