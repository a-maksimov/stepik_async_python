import asyncio


def check_loop_status(loop):
    return f'Цикл событий активен: {loop.is_running()}, Цикл событий закрыт: {loop.is_closed()}.'


async def main():
    print(check_loop_status(loop))
    print("Корутина завершена")


loop = asyncio.new_event_loop()
print(check_loop_status(loop))
loop.run_until_complete(main())
loop.close()
print(check_loop_status(loop))

