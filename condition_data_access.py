import asyncio

# Имена пользователей
users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eva', 'Frank', 'George', 'Helen', 'Ivan', 'Julia']


async def data_access(user, condition):
    async with condition:
        print(f"Пользователь {user} ожидает доступа к базе данных")
        await condition.wait()
        print(f"Пользователь {user} подключился к БД")
        await asyncio.sleep(0.5)
        print(f"Пользователь {user} отключается от БД")
        condition.notify()


# корутина, отправляющая уведомление
async def notifying_coro(condition):
    async with condition:
        condition.notify_all()


async def main():
    condition = asyncio.Condition()
    tasks = asyncio.gather(*[data_access(user, condition) for user in users])
    asyncio.create_task(notifying_coro(condition))
    await tasks


if __name__ == "__main__":
    asyncio.run(main())
