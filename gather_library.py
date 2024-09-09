# Полный десериализованый JSON вшит в задачу
import asyncio

books_json = [
    {
        "Порядковый номер": 1,
        "Автор": "Rebecca Butler",
        "Название": "Three point south wear score organization.",
        "Год издания": "1985",
        "Наличие на полке": False
    },
    {
        "Порядковый номер": 2,
        "Автор": "Mark Cole",
        "Название": "Drive experience customer somebody pressure.",
        "Год издания": "1985",
        "Наличие на полке": True
    },
]


async def check_book(book):
    return book['Наличие на полке']


async def main():
    tasks = [
        asyncio.create_task(check_book(book))
        for book
        in books_json
    ]
    results = await asyncio.gather(*tasks)
    for result, book in zip(results, books_json):
        if result:
            continue

        print(f'{book["Порядковый номер"]}: {book["Автор"]}: {book["Название"]} ({book["Год издания"]})')


asyncio.run(main())
