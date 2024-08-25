import asyncio


log_events = [
    {"event": "Запрос на вход", "delay": 0.5},
    {"event": "Запрос данных пользователя", "delay": 1.0},
    {"event": "Обновление данных пользователя", "delay": 1.5},
    {"event": "Обновление конфигурации сервера", "delay": 5.0}
    ]


async def fetch_log_event(event):
    event_name = event["event"]
    await asyncio.sleep(event["delay"])
    return print(f"Событие: '{event_name}' обработано с задержкой {event['delay']} сек.")


async def main():
    tasks = [fetch_log_event(event) for event in log_events]
    await asyncio.gather(*tasks)

asyncio.run(main())