import asyncio
from itertools import product

# Словарь заклинаний со временем каста
# Полный словарь заклинаний вшит в задачу
spells = {
    "Огненный шар": 3,
    "Ледяная стрела": 2,
    "Щит молний": 4,
    "Телепортация": 7
}

# Ученики мага
students = ["Алара", "Бренн", "Сирил", "Дариа", "Элвин"]

# Максимальное время для каста заклинания
max_cast_time = 5  # Секунды


async def cast(cast_time):
    await asyncio.sleep(cast_time)


async def cast_shield(student, spell, cast_time):
    task = asyncio.create_task(cast(cast_time))
    try:
        await asyncio.wait_for(asyncio.shield(task), max_cast_time)
        print(f"{student} успешно кастует {spell} за {cast_time} сек.")
    except TimeoutError:
        await task
        print(f"Ученик {student} не справился с заклинанием {spell}, и учитель применил щит. {student} успешно завершает заклинание с помощью shield.")


async def main():
    tasks = [cast_shield(student, spell, spells[spell]) for student, spell in product(students, spells)]
    await asyncio.gather(*tasks, return_exceptions=True)


asyncio.run(main())
