import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from parser import parse_avito_page
from loadenv import Envi  # Импорт обработчика переменных окружения

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Загрузка переменных окружения
env = Envi()
API_TOKEN = env.telegram_api

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Отправь мне ссылку на страницу Avito, и я выдам тебе нужные данные.")

# Обработчик текстовых сообщений (ссылок на Avito)
@dp.message_handler()
async def parse_avito(message: types.Message):
    url = message.text
    try:
        # Парсинг страницы
        data = parse_avito_page(url)
        response = f"Заголовок: {data['title']}\nЦена: {data['price']}"
    except Exception as e:
        response = f"Ошибка при парсинге страницы: {e}"
    await message.reply(response)

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)