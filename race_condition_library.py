import asyncio

# Библиотечный каталог
library_catalog = {
    "Мастер и Маргарита": 3,
    "Война и мир": 2,
    "Преступление и наказание": 1,
}

# Резервирование книг для пользователей
reservation_tasks = {
    "Алексей": "Мастер и Маргарита",
    "Ирина": "Мастер и Маргарита",
    "Сергей": "Война и мир",
    "Елена": "Преступление и наказание",
    "Анна": "Мастер и Маргарита",
    "Игорь": "Война и мир",
    "Мария": "Преступление и наказание",
}


async def reserve_book(book):
    value = library_catalog[book]
    await asyncio.sleep(1)
    if value > 0:
        library_catalog[book] -= 1
        print("Книга успешно зарезервирована.")
    else:
        print("Книга отсутствует. Резервирование отменено.")


async def main():
    tasks = [reserve_book(book) for book in reservation_tasks.values()]
    await asyncio.gather(*tasks)

    for book, value in library_catalog.items():
        print(f"{book}: {value}")


asyncio.run(main())
