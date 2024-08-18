import asyncio

students = {
    'Алекс': 5,
    'Мария': 3,
    'Иван': 4
}


async def read_book(student, time):
    print(f"{student} начал читать книгу.")
    await asyncio.sleep(time)
    print(f"{student} закончил читать книгу за {time} секунд.")


async def main():
    tasks = []
    for student, time in students.items():
        tasks.append(read_book(student, time))
    await asyncio.gather(*tasks)


asyncio.run(main())
