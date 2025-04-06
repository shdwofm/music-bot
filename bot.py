import os  # <--- Этого не хватало!
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from link_converter import get_alt_link

# Получение токена из переменной окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("Переменная окружения BOT_TOKEN не установлена")

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализация бота и диспетчера
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())

# Обработчик команды /start
@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("🎵 Привет! Отправь мне ссылку на песню, а в ответ я пришлю тебе ссылки на другие стриминги.")

# Обработка сообщений со ссылками
@dp.message()
async def link_handler(message: Message):
    original_url = message.text.strip()

    target_platforms = ["spotify", "appleMusic", "youtube", "deezer", "soundcloud"]  # убрал пока yandex
    responses = []

    for platform in target_platforms:
        alt_link = get_alt_link(original_url, platform)
        if alt_link:
            responses.append(f"<b>{platform.capitalize()}</b>: <a href=\"{alt_link}\">{alt_link}</a>")

    if responses:
        await message.answer("\n\n".join(responses))
    else:
        await message.answer("❌ Не получилось найти альтернативу. Проверь ссылку.")

# Запуск бота
if __name__ == "__main__":
    dp.run_polling(bot)
