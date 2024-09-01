import asyncio

reports = [
    {"name": "Алексей Иванов", "report": "Отчет о прибылях и убытках", "load_time": 5},
    {"name": "Мария Петрова", "report": "Прогнозирование движения денежных средств", "load_time": 4},
    {"name": "Иван Смирнов", "report": "Оценка инвестиционных рисков", "load_time": 3},
    {"name": "Елена Кузнецова", "report": "Обзор операционных расходов", "load_time": 2},
    {"name": "Дмитрий Орлов", "report": "Анализ доходности активов", "load_time": 10}
]


async def download_data(report):
    name = report['name']
    report_name = report['report']

    if name == 'Дмитрий Орлов':
        await cancel_task(asyncio.current_task())
        print(f"Загрузка отчета {report_name} для пользователя {name} остановлена. Введите новые данные")
        return

    await asyncio.sleep(report['load_time'])
    print(f"Отчет: {report_name} для пользователя {name} готов")


async def cancel_task(task):
    task.cancel()


async def main():
    tasks = [download_data(report) for report in reports]
    await asyncio.gather(*tasks, return_exceptions=True)

asyncio.run(main())
