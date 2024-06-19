import telebot
from config.settings import TELEGRAM_API_TOKEN
from bot.handlers import command_handlers, mood_handlers, db_handler

try:
    # Initialize the database
    db_handler.register()
except Exception as e:
    print(f"Error initializing database: {e}")

# Create the bot instance
bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

# Register command handlers and mood handlers
command_handlers.register(bot)
mood_handlers.register(bot)

if __name__ == '__main__':
    try:
        print('Bot is running...')
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Error occurred while running the bot: {e}")
