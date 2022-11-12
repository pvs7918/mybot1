# pip install python-telegram-bot --pre
# python bot.py

# Адрес бота
# http://t.me/my_cross_zero_bot


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}, давай сыграем в крестики-нолики. /step номер позиции (от 1 до 9)')

async def step(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Step {update.effective_user.first_name}')
    # msg = update.message.text
    # print(msg)
    # update.message.reply_text(f'{msg}')


app = ApplicationBuilder().token("5730417154:AAFsc0RyGQzocF395dcKcuIhBZAJBFr0Aa8").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("step", step))
print('Telegram bot run')
app.run_polling()