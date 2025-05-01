import os
import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Настройка логов
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Получение токена из переменной окружения
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    logger.error("Переменная окружения BOT_TOKEN не найдена!")
    raise ValueError("Переменная окружения BOT_TOKEN не найдена!")

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    logger.info(f"Пользователь {user.id} ({user.first_name}) начал взаимодействие с ботом.")

    keyboard = [
        [KeyboardButton(text="Открыть Квиз", web_app=WebAppInfo(url="https://kvizapp.vercel.app"))]
    ]
    await update.message.reply_text(
        "Нажми кнопку чтобы открыть квиз!",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

# Обработка данных, полученных из WebApp
async def handle_web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.web_app_data.data
    await update.message.reply_text(f"Ты отправил: {data}")

# Запуск бота
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_web_app_data))
    app.run_polling()

if __name__ == "__main__":
    main()
