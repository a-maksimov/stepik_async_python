import asyncio
import time


async def process_request(request_name, stages, status):
    for stage_name in stages:
        await asyncio.sleep(0)
        time.sleep(1)  # Симулируем время выполнения этапа
        status[request_name] = f"{stage_name}"


async def update_status(request_name, status):
    while True:
        await asyncio.sleep(0)
        print(status)
        if status == {request_name: 'Отправка уведомлений'}:
            break


async def main():
    # Исходные данные по запросу и этапам его обработки
    request_name = 'Запрос 1'
    stages = ["Загрузка данных", "Проверка данных", "Анализ данных", "Сохранение результатов", "Отправка уведомлений"]

    status = {request_name: None}

    # Создание задач для каждой корутины
    process_task = asyncio.create_task(process_request(request_name, stages, status))
    updater_task = asyncio.create_task(update_status(request_name, status))

    await asyncio.gather(process_task, updater_task)


asyncio.run(main())

# {'Запрос 1': 'Загрузка данных'}
# {'Запрос 1': 'Проверка данных'}
# {'Запрос 1': 'Анализ данных'}
# {'Запрос 1': 'Сохранение результатов'}
# {'Запрос 1': 'Отправка уведомлений'}
