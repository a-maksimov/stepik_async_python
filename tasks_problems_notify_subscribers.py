import asyncio


async def publish_post(text):
    await asyncio.sleep(1)
    print(f"Пост опубликован: {text}")
    return f"Пост опубликован: {text}"


async def notify_subscriber(subscriber):
    await asyncio.sleep(1)
    print(f"Уведомление отправлено {subscriber}")


async def notify_subscribers(subscribers):
    tasks = [notify_subscriber(subscriber) for subscriber in subscribers]
    await asyncio.gather(*tasks)


async def main():
    post_text = "Hello world!"
    subscribers = ["Alice", "Bob", "Charlie", "Dave", "Emma", "Frank", "Grace", "Henry", "Isabella", "Jack"]
    publish = asyncio.create_task(publish_post(post_text))
    notify = asyncio.create_task(notify_subscribers(subscribers))
    await asyncio.gather(publish, notify)


asyncio.run(main())
