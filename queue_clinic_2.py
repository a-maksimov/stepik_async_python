import asyncio

patient_info = [
    {'name': 'Алексей Иванов', 'direction': 'Терапевт', 'procedure': 'Прием для общего осмотра'},
    {'name': 'Мария Петрова', 'direction': 'Хирург', 'procedure': 'Малая операция'},
    {'name': 'Ирина Сидорова', 'direction': 'ЛОР', 'procedure': 'Осмотр уха'},
    {'name': 'Владимир Кузнецов', 'direction': 'Терапевт', 'procedure': 'Консультация'},
    {'name': 'Елена Васильева', 'direction': 'Хирург', 'procedure': 'Хирургическая процедура'},
    {'name': 'Дмитрий Николаев', 'direction': 'ЛОР', 'procedure': 'Промывание носа'},
    {'name': 'Светлана Михайлова', 'direction': 'Терапевт', 'procedure': 'Рутинный осмотр'},
    {'name': 'Никита Алексеев', 'direction': 'Хирург', 'procedure': 'Операция на колене'},
    {'name': 'Ольга Сергеева', 'direction': 'ЛОР', 'procedure': 'Лечение ангины'},
    {'name': 'Анна Жукова', 'direction': 'Терапевт', 'procedure': 'Вакцинация'}
]


async def producer(queues, patient_info):
    for patient in patient_info:
        await asyncio.sleep(0.5)
        await queues[patient["direction"]].put(patient)

        print(
            f"Регистратор добавил в очередь: {patient['name']}, направление: {patient['direction']}, процедура: {patient['procedure']}")

    for queue in queues.values():
        await queue.put(None)


async def consumer(queue, doctor_type):
    while True:
        await asyncio.sleep(0.5)
        patient = await queue.get()
        if patient is None:
            break

        print(f"{doctor_type} принял пациента: {patient['name']}, процедура: {patient['procedure']}")


async def main():
    directions = {procedure["direction"] for procedure in patient_info}
    queues = {}

    for direction in directions:
        queues[direction] = asyncio.Queue()

    producer_task = asyncio.create_task(producer(queues, patient_info))

    consumer_tasks = []
    for doctor_type, queue in queues.items():
        consumer_tasks.append(asyncio.create_task(consumer(queue, doctor_type)))

    await asyncio.gather(producer_task, *consumer_tasks)


asyncio.run(main())
