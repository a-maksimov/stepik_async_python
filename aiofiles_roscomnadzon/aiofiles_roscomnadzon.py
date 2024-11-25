import asyncio
import json
import os
import re
import aiofiles

semaphore = asyncio.Semaphore(100)

pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} - ([А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+): (.+)'


async def process_file(filename):
    result = {}

    folder = 'chat_log'
    filename = f'{folder}\\{filename}'
    async with semaphore:
        async with aiofiles.open(filename, 'r', encoding='utf-8') as file:
            async for line in file:
                match = re.search(pattern, line)
                if match:
                    name = match.group(1)
                    message = match.group(2)
                    value = len(message) * 0.03
                    result[name] = result.get(name, 0) + value

    return result


async def main():
    tasks = []
    for filename in os.listdir("chat_log"):
        tasks.append(process_file(filename))

    results = await asyncio.gather(*tasks)

    global_result = {}
    for result in results:
        for name, value in result.items():
            global_result[name] = global_result.get(name, 0) + value

    sorted_result = dict(sorted(global_result.items(), key=lambda item: item[1], reverse=True))

    # Formatting values
    formatted_result = {
        name: f"{round(value, 2):0{6}}р"
        for name, value in sorted_result.items()
    }

    # Write formatted results to a JSON file
    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(formatted_result, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    asyncio.run(main())
