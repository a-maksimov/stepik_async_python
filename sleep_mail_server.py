import asyncio
import random

# Не менять.
random.seed(1)


class MailServer:
    def __init__(self):
        self.mailbox = ["Привет!", "Встреча в 15:00", "Важное уведомление", "Реклама"]

    async def check_for_new_mail(self):
        if random.random() < 0.1:
            return "Ошибка при проверке новых писем."
        return random.choice([True, False])

    async def fetch_new_mail(self):
        mail = random.choice(self.mailbox)
        return f"Новое письмо: {mail}"


# Тут пишите ваш код
async def check_mail(server):
    while True:
        await asyncio.sleep(1)
        result = await server.check_for_new_mail()
        if result is True:
            mail = await server.fetch_new_mail()
            print(mail)
        elif result is False:
            print("Новых писем нет.")
        else:
            print(result)
            return


async def main():
    mail_server = MailServer()
    await check_mail(mail_server)

asyncio.run(main())