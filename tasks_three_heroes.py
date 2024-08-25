import asyncio

places = [
    "начинает путешествие",
    "находит загадочный лес",
    "переправляется через реку",
    "встречает дружелюбного дракона",
    "находит сокровище"]

names = [
    'Искатель приключений',
    'Храбрый рыцарь',
    'Отважный пират'
]


async def counter(name, delay=0.1):
    for place in places:
        await asyncio.sleep(delay)
        print(f"{name} {place}...")


async def main():
    tasks = [counter(name) for name in names]
    await asyncio.gather(*tasks)

asyncio.run(main())
