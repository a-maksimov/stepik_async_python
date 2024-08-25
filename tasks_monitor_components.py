import asyncio


async def monitor_cpu(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        print(f"[{task_name}] Статус проверки: {status}")
        if status == 'Катастрофически':
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            return
        await asyncio.sleep(0)


async def monitor_memory(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        print(f"[{task_name}] Статус проверки: {status}")
        if status == 'Катастрофически':
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            return
        await asyncio.sleep(0)


async def monitor_disk_space(status_list):
    task_name = asyncio.current_task().get_name()
    for status in status_list:
        print(f"[{task_name}] Статус проверки: {status}")
        if status == 'Катастрофически':
            print(f"[{task_name}] Критическое состояние достигнуто. Инициируется остановка...")
            return
        await asyncio.sleep(0)


async def main():
    status_list = [
        "Отлично", "Хорошо", "Удовлетворительно", "Средне",
        "Пониженное", "Ниже среднего", "Плохо", "Очень плохо",
        "Критично", "Катастрофически"
    ]

    monitor_cpu_task = asyncio.create_task(monitor_cpu(status_list), name="CPU")
    monitor_memory_task = asyncio.create_task(monitor_cpu(status_list), name="Память")
    monitor_disk_space_task = asyncio.create_task(monitor_cpu(status_list), name="Дисковое пространство")

    await asyncio.gather(monitor_cpu_task, monitor_memory_task, monitor_disk_space_task)


asyncio.run(main())
