import asyncio

students = {
    "Алекс": {"course": "Асинхронный Python", "steps": 515, "speed": 78},
    "Мария": {"course": "Многопоточный Python", "steps": 431, "speed": 62},
    "Иван": {"course": "WEB Парсинг на Python", "steps": 491, "speed": 57}
}


async def study_course(student, course, steps, speed):
    reading_time = steps / speed
    print(f'{student} начал проходить курс {course}.')
    await asyncio.sleep(reading_time)
    return student, course, reading_time


async def main():
    tasks = []
    for student, data in students.items():
        course, steps, speed = data['course'], data['steps'], data['speed']
        tasks.append(asyncio.create_task(study_course(student, course, steps, speed)))
    await asyncio.gather(*tasks)

    for task in tasks:
        student, course, time = task.result()
        print(f'{student} прошел курс {course} за {round(time, 2)} ч.')

asyncio.run(main())
