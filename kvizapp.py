
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8070824455:AAG-y_oSvl78o8wq3jKr_VWGsQlBnQ6Bkkc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton(text="Открыть мини-приложение", web_app=WebAppInfo(url="https://https://kvizapp.vercel.app"))]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Нажми кнопку ниже:", reply_markup=reply_markup)

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()

from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8070824455:AAG-y_oSvl78o8wq3jKr_VWGsQlBnQ6Bkkc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton(text="Открыть мини-приложение", web_app=WebAppInfo(url="https://kvizapp-git-main-marianmykolas-projects.vercel.app"))]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Нажми кнопку ниже:", reply_markup=reply_markup)

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()

