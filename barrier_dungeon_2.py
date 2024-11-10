import asyncio

players = {
    'DragonSlayer': 0.2,
    'ShadowHunter': 0.6,
    'MagicWizard': 0.8,
    'ElfArcher': 2.0,
    'DarkMage': 1.4,
    'SteelWarrior': 1.6,
    'ThunderBolt': 3.0
}

barrier = asyncio.Barrier(5)


async def enter_dungeon(player):
    await asyncio.sleep(players[player])
    print(f"{player} готов войти в подземелье")
    try:
        await asyncio.wait_for(barrier.wait(), 5)
        print(f"{player} вошел в подземелье")
    except asyncio.TimeoutError:
        print(f"{player} не смог попасть в подземелье. Группа не собрана")


async def main():
    tasks = [enter_dungeon(player) for player in players]
    await asyncio.gather(*tasks, return_exceptions=True)
    await barrier.reset()


asyncio.run(main())
