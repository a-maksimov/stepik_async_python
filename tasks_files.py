import asyncio

files = {
    "file1.mp4": 32,
    "image2.png": 24,
    "audio3.mp3": 16,
    "document4.pdf": 8,
    "archive5.zip": 40,
    "video6.mkv": 48,
    "presentation7.pptx": 12,
    "ebook8.pdf": 20,
    "music9.mp3": 5,
    "photo10.jpg": 7,
    "script11.py": 3,
    "database12.db": 36,
    "archive13.rar": 15,
    "document14.docx": 10,
    "spreadsheet15.xls": 25,
    "image16.gif": 2,
    "audioBook17.mp3": 60,
    "tutorial18.mp4": 45,
    "code19.zip": 22,
    "profile20.jpg": 9
}


async def download_file(filename, file_size, bandwidth=8):
    delay = file_size / bandwidth
    print(f'Начинается загрузка файла: {filename}, его размер {file_size} мб, время загрузки составит {delay} сек')
    await asyncio.sleep(delay)
    print(f'Загрузка завершена: {filename}')


async def monitor_tasks(tasks):
    done = []
    await asyncio.sleep(0)
    while len(done) < len(tasks):
        for task in tasks:
            if task.done():
                if task not in done:
                    print(f"Задача {task.get_name()}: завершена, Статус задачи {task.done()}")
                    done.append(task)
            else:
                print(f"Задача {task.get_name()}: в процессе, Статус задачи {task.done()}")
        await asyncio.sleep(1)
    for task in done:
        print(f"Задача {task.get_name()}: завершена, Статус задачи {task.done()}")


async def main():
    tasks = [
        asyncio.create_task(download_file(filename, file_size))
        for filename, file_size in files.items()
    ]
    [task.set_name(filename) for task, filename in zip(tasks, files)]
    await monitor_tasks(tasks)
    print('Все файлы успешно загружены')


asyncio.run(main())
