# Import necessary modules
import telebot
import os
from random import choice

# Get the token from the environment variables
token = os.environ.get('API_TOKEN')

# Create the bot using the token
bot = telebot.TeleBot(token)

# Define lists of responses for different moods
happy = [
    "Believe you can and you're halfway there.",
    "You are stronger than you think.",
    "Keep pushing forward, no matter what."
]

sad = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why was the math book sad? Because it had too many problems.",
    "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats!"
]

angry = [
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one!"
]

# Handle the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Send welcome messages to the user
    bot.send_message(message.chat.id, "Hello!")
    bot.send_message(message.chat.id, "I am a chatbot created to keep you smiling and motivated.😊")
    bot.send_message(message.chat.id, "How are you Feeling today?\n\nPlease type 'Happy', 'Sad' or 'Angry' to let me know!😊")

# Handle all messages
@bot.message_handler(func=lambda message : True)
def mood_response(message):
    # Define a dictionary to map moods to responses
    mood_dict = {
        'happy': choice(happy),
        'sad': choice(sad),
        'angry': choice(angry)
    }

    # Get the mood from the message text
    mood = message.text.lower()

    # Get the response for the mood, or a default response if the mood is not found
    response = mood_dict.get(mood, "I am sorry! I am not trained to understand that!😊")

    # Send the response to the user
    bot.send_message(message.chat.id, response)

# Start the bot
bot.polling()