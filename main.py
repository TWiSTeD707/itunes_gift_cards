import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.types.web_app_info import WebAppInfo
from django.urls import path
from templates.views import itunes_gift_cards

urlpatterns = [
    path('itunes-gift-cards/', itunes_gift_cards, name='itunes_gift_cards'),
]

API_TOKEN = '6902201735:AAG38t37cVKqbEAi82uQNS-2cqeGPTzF24E'  # Замените на ваш токен бота

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    chat_id = message.chat.id
    markup = InlineKeyboardMarkup()
    url_button = InlineKeyboardButton(text="Перейти в приложение", web_app=WebAppInfo(url="https://www.pythonanywhere.com/user/dev11100100/files/home/dev11100100/itunes_gift_cards/itunes_gift_cards.html"))
    markup.add(url_button)
    await bot.send_message(chat_id,
                           "Добро пожаловать! Для покупки карточек iTunes перейдите по ссылке на наше веб-приложение "
                           "в Telegram:",
                           reply_markup=markup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

