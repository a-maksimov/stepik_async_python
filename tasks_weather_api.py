import asyncio
import random

# Не менять!
random.seed(0)


async def fetch_weather(source, city):
    await asyncio.sleep(random.randint(0, 5))
    temperature = random.randint(-10, 35)
    return f"Данные о погоде получены из источника {source} для города {city}: {temperature}°C"


async def main():
    city = "Москва"
    sources = [
        'http://api.weatherapi.com',
        'http://api.openweathermap.org',
        'http://api.weatherstack.com',
        'http://api.weatherbit.io',
        'http://api.meteostat.net',
        'http://api.climacell.co'
    ]
    tasks = [asyncio.create_task(fetch_weather(source, city)) for source in sources]
    done, _ = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(next(iter(done)).result())

asyncio.run(main())
