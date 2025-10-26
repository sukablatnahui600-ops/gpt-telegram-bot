import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from openai import OpenAI

# Создаём объекты
bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))
dp = Dispatcher(bot)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@dp.message_handler()
async def handle_message(message: types.Message):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # можно заменить на gpt-4o
            messages=[{"role": "user", "content": message.text}]
        )
        await message.answer(response.choices[0].message.content)
    except Exception as e:
        await message.answer("Произошла ошибка 😅")
        print(e)

if __name__ == "__main__":
    print("Бот запущен...")
    executor.start_polling(dp, skip_updates=True)
