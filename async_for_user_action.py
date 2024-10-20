import asyncio
import random

users = ['user1', 'user2', 'user3']
products = ['iPhone 14', 'Samsung Galaxy S23', 'MacBook Pro', 'Dell XPS 13', 'Sony WH-1000XM5', 'Apple Watch Series 8',
            'Kindle Paperwhite', 'GoPro Hero 11', 'Nintendo Switch', 'Oculus Quest 2']
actions = ['просмотр', 'покупка', 'добавление в избранное']


async def user_action_generator():
    while True:
        yield {'user_id': random.choice(users), 'action': random.choice(actions), 'product_id': random.choice(products)}


async def main():
    async for action in user_action_generator():
        print(action)


asyncio.run(main())
