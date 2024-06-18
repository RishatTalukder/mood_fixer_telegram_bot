import telebot 
from config.settings import TELEGRAM_API_TOKEN
from bot.handlers import command_handlers, mood_handlers

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

command_handlers.register(bot)
mood_handlers.register(bot)

if __name__ == '__main__':
    bot.polling(none_stop=True)
    print('Bot is running...')