import asyncio
import contextvars

current_language = contextvars.ContextVar('current_language')


def set_language(language_code):
    current_language.set(language_code)


async def get_greeting():
    greetings = {
        'en': "Hello!",
        'ru': "Привет!",
        'es': "Hola!"
    }
    return greetings[current_language.get()]


async def get_error_message():
    error_messages = {
        'en': "An error occurred.",
        'ru': "Произошла ошибка.",
        'es': "Ocurrió un error."
    }
    return error_messages[current_language.get()]


async def test_user_actions(language_code):
    current_language.set(language_code)
    msg = await get_greeting()
    print(msg)
    msg = await get_error_message()
    print(msg)


async def main():
    tasks = [test_user_actions(language_code) for language_code in ['en', 'ru', 'es']]
    await asyncio.gather(*tasks)


asyncio.run(main())
