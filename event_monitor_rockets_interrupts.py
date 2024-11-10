import asyncio
import random

error = None
count = 0
sek = 0


async def monitor_rocket_launches(interrupt_flag):
    global count
    global error
    global sek
    try:
        # Допишите сюда цикл
        while True:
            if interrupt_flag.is_set():
                asyncio.current_task().cancel()
                break
            sek += 1
            count += 1
            error = random.choices([True, None], weights=[25, 75])[0]
            print(f"Мониторинг ракетных запусков... (Запуск номер {count} прошёл успешно)")
            await asyncio.sleep(1)
    finally:
        # Поместите сообщение о завершении мониторинга
        print("Завершение мониторинга ракетных запусков")


async def main():
    global error
    global count
    global sek
    event = asyncio.Event()
    task = asyncio.create_task(monitor_rocket_launches(event))

    while True:
        await asyncio.sleep(5)
        if count == 50:
            event.set()
            break
        elif error:
            print(f"Ошибка при запуске произошла на {sek} секунде =(")
            print("Отмена мониторинга ракетных запусков...")
            event.set()
            break
        else:
            print(f"Время ожидания составило {sek} секунд. За это время ошибки не произошло")

    # Запустите созданную корутину в пункте 2 через await
    try:
        await task
    except asyncio.CancelledError:
        pass


if __name__ == "__main__":
    asyncio.run(main())
