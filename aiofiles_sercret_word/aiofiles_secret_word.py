import asyncio
import os
import aiofiles

words = [
    'дом', 'море', 'солнце', 'небо', 'лес', 'река', 'гора', 'птица', 'цветок', 'жизнь',
    'любовь', 'работа', 'друг', 'снег', 'вода', 'ветер', 'огонь', 'поля', 'города', 'день',
    'ночь', 'мост', 'улица', 'поезд', 'парк', 'здание', 'площадь', 'дождь', 'собака', 'кошка',
    'свет', 'тень', 'игра', 'песок', 'книга', 'город', 'песня', 'звезда', 'механизм', 'автомобиль',
    'поездка', 'путешествие', 'молоко', 'хлеб', 'яйцо', 'фрукт', 'овощ', 'журнал', 'газета', 'кафе',
    'ресторан', 'рецепт', 'вино', 'чай', 'кофе', 'письмо', 'письменность', 'рука', 'ноги', 'часы',
    'календарь', 'зеркало', 'стол', 'стул', 'диван', 'шкаф', 'завтрак', 'обед', 'ужин', 'горы',
    'реки', 'поля', 'море', 'океан', 'пляж', 'солнечный', 'дождливый', 'ветряный', 'холодный', 'тёплый',
    'лето', 'зима', 'весна', 'осень', 'страна', 'континент', 'планета', 'звезда', 'галактика', 'космос',
    'мир', 'человек', 'семья', 'родители', 'дети', 'сестра', 'брат', 'дедушка', 'бабушка', 'дядя',
    'тётя', 'кукла', 'игрушка', 'тренировка', 'спорт', 'футбол', 'баскетбол', 'волейбол', 'тренер', 'спортзал',
    'кухня', 'спальня', 'ванная', 'коридор', 'гараж', 'сад', 'огород', 'площадка', 'гостинная', 'столовая',
    'интернет', 'телефон', 'компьютер', 'телевизор', 'фильм', 'сериал', 'новости', 'погода', 'прогноз', 'город',
    'посёлок', 'деревня', 'село', 'улица', 'переулок', 'площадь', 'парк', 'горы', 'лес', 'пещера', 'водопад',
    'озеро', 'рыба', 'мясо', 'суп', 'бульон', 'пирог', 'пицца', 'паста', 'салат', 'десерт', 'торт', 'пирожное'
]


async def process_file(filename, event):
    folder = 'files_with_secret_word'
    filepath = f'{folder}\\{filename}'
    async with aiofiles.open(filepath, mode='r', encoding='utf-8') as f:
        async for line in f:
            if not event.is_set():
                for word in line.split():
                    if word.strip() not in words:
                        event.set()
                        print(f'{filename}: {word}')
                        await asyncio.sleep(0)
                        break
            else:
                break


async def main():
    event = asyncio.Event()
    tasks = []
    for i, file in enumerate(os.listdir("files_with_secret_word")):
        tasks.append(process_file(file, event))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())