from telebot import TeleBot

def register(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        """
        This function sends a welcome message to the user when the /start command is received.
        """
        bot.send_message(message.chat.id, "Hello!")
        bot.send_message(message.chat.id, "I am a chatbot created to keep you smiling and motivated.😊")
        bot.send_message(message.chat.id, "How are you Feeling today?\n\nPlease type 'Happy', 'Sad' or 'Angry' to let me know!😊")