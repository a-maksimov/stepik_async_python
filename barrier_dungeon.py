import asyncio

players = {
    'DragonSlayer': 0.2,
    'ShadowHunter': 0.6,
    'MagicWizard': 0.8,
    'KnightRider': 0.3,
    'ElfArcher': 2.0,
    'DarkMage': 1.4,
    'SteelWarrior': 1.6,
    'ThunderBolt': 3.0,
    'SilentAssassin': 1.1,
    'FireSorcerer': 2.6,
    'MysticHealer': 1.5,
    'IceQueen': 1.7,
    'BladeMaster': 2.9,
    'StormBringer': 1.2,
    'ShadowKnight': 0.9,
    'GhostRogue': 1.8,
    'FlameWielder': 0.7,
    'ForestGuardian': 0.4,
    'BattlePriest': 1.9,
    'EarthShaker': 2.8
}

barrier = asyncio.Barrier(5)


async def enter_dungeon(player):
    await asyncio.sleep(players[player])
    print(f"{player} готов войти в подземелье")
    await barrier.wait()
    print(f"{player} вошел в подземелье")


async def main():
    tasks = [enter_dungeon(player) for player in players]
    await asyncio.gather(*tasks)


asyncio.run(main())
