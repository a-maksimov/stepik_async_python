import asyncio

codes = ["56FF4D", "A3D2F7", "B1C94A", "F56A1D", "D4E6F1",
         "A1B2C3", "D4E5F6", "A7B8C9", "D0E1F2", "A3B4C5",
         "D6E7F8", "A9B0C1", "D2E3F4", "A5B6C7", "D8E9F2"]

messages = ["Привет, мир!", "Как дела?", "Что нового?", "Добрый день!", "Пока!",
            "Спокойной ночи!", "Удачного дня!", "Всего хорошего!", "До встречи!", "Счастливого пути!",
            "Успехов в работе!", "Приятного аппетита!", "Хорошего настроения!", "Спасибо за помощь!",
            "Всего наилучшего!"]


def print_code(task):
    print(f'Код: {task.result()}')


async def print_message(message, code):
    if (code[-1] == '0' or code[-1] == '2' or
            code[-1] == '4' or code[-1] == '6' or
            code[-1] == '8' or code[-1] == 'A' or
            code[-1] == 'C' or code[-1] == 'E'):
        print('Сообщение: Неверный код, сообщение скрыто')
    else:
        print(f'Сообщение: {message}')

    return code


async def main():
    for message, code in zip(messages, codes):
        task = asyncio.create_task(print_message(message, code))
        task.add_done_callback(print_code)
        await task


asyncio.run(main())
