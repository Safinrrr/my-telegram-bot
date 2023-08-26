from telegram import Bot
from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text("Привет! Я ваш бот.")

def main():
    token = "6596347347:AAGcRtZ1FOXz0Wt4PymaXzOhZO40vqHDf2A"
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
