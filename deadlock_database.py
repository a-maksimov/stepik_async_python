import asyncio

number_facts_database = {
    1: "Один — это единственное число, которое не является ни простым, ни составным.",
    2: "Десять — это база десятичной системы счисления, которую мы используем ежедневно."
}


async def get_fact_from_db(lock, number):
    await asyncio.sleep(number * 0.1)
    global number_facts_database
    async with lock:
        print(f'{number}: {number_facts_database[number]}')


async def main():
    lock = asyncio.Lock()
    tasks = [asyncio.create_task(get_fact_from_db(lock, i)) for i in range(1, len(number_facts_database) + 1)]
    await asyncio.gather(*tasks)


asyncio.run(main())
