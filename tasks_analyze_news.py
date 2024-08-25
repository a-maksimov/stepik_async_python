import asyncio

keywords = {
    "COVID-19": 1,
    "игр": 1,
    "новый вид": 1,
}


news_list = [
    "Новая волна COVID-19 обрушилась на Европу",
    "Рынки акций растут на фоне новостей о вакцине",
]


async def analyze_news(keyword, news_list, delay=1):
    await asyncio.sleep(delay)
    for news in news_list:
        if keyword not in news:
            continue
        print(f"Найдено соответствие для '{keyword}': {news}")
        await asyncio.sleep(0)


async def main():
    # Создаем асинхронные задачи для каждой корутины с разными ключевыми словами и задержками
    tasks = [analyze_news(keyword, news_list, delay) for keyword, delay in keywords.items()]

    # Ожидаем выполнения всех задач
    await asyncio.gather(*tasks)

asyncio.run(main())