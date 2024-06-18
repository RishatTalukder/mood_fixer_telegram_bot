from telebot import TeleBot
from bot.utils.responses import get_mood_response

def register(bot: TeleBot):
    @bot.message_handler(func=lambda message: True)
    def mood_response(message):
        """
        This function sends a message to the user when the /mood command is received.
        """
        response = get_mood_response(message.text.lower())
        bot.send_message(message.chat.id, response)