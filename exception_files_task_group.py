import asyncio

files = ['image.png', 'file.csv', 'file1.txt']  # полный список вшит в задачу


# Не менять функцию
async def download_file(file_name):
    ...
    # функция вшита в задачу, она имитирует скачивание файла с сервера, генерирует несколько типов ошибок:
    # raise FileNotFoundError(f'{file_name}: Файл не найден')
    # raise PermissionError(f'{file_name}: Нет прав на доступ к файлу')
    # raise TimeoutError(f'{file_name}: Превышено время ожидания для скачивания файла')


# Ваш код пишите тут:
async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            [tg.create_task(download_file(file)) for file in files]
    except* FileNotFoundError as e:
        for error in e.exceptions:
            print(error)
    except* PermissionError as e:
        for error in e.exceptions:
            print(error)
    except* TimeoutError as e:
        for error in e.exceptions:
            print(error)


asyncio.run(main())
