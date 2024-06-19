import telebot
from config.settings import TELEGRAM_API_TOKEN
from bot.handlers import command_handlers, mood_handlers, db_handler

# Initialize the database
db_handler.register()

# Create the bot instance
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

# Register command handlers and mood handlers
command_handlers.register(bot)
mood_handlers.register(bot)

if __name__ == '__main__':
    print('Bot is running...')
    bot.polling(none_stop=True)
