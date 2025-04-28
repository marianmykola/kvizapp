import os
import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Настройка логов
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Получение токена
BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    logger.error("Переменная окружения BOT_TOKEN не найдена!")
    raise ValueError("Переменная окружения BOT_TOKEN не найдена!")

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    logger.info(f"Пользователь {user.id} ({user.first_name}) начал взаимодействие с ботом.")
    
    keyboard = [
        [KeyboardButton(text="Открыть мини-приложение", web_app=WebAppInfo(url="https://kvizapp.vercel.app"))]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text("Нажми кнопку ниже:", reply_markup=reply_markup)

# Инициализация приложения
app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

# Запуск бота
app.run_polling()
