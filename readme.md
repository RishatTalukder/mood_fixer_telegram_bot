# Mood Fixer

`Mood fixer` is a telegram bot that helps you to improve your mood by providing you with a variety of activities Like `Jokes`, `motivational quotes`,`music` and `movies` to watch.

This readme file contains all the information you need to know about the bot and also how to build it yourself.

## Start

To start making the bot you need to have a telegram account. Then search for `@BotFather` in the search bar and click on it. 

> Bot father is the official bot that helps you to create a new bot.

This will take you to the bot father chat. Now follow this steps to create a new bot.

- Click on the start button.
- Click on the `/newbot` command.
- Now you need to give a name to your bot. This name will be displayed in the chat. The bot must have a unique name and a `bot` suffix. For example, `MoodFixer_bot`.

If the name is unique then you will get a message like this.

```
Done! Congratulations on your new bot. You will find it at t.me/MoodFixer_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

```

``` Use this `secret token`(secret API key) to access the HTTP API: `your secret token` ```

Now you have successfully created a new bot. Now we can go to the main part of the project.

## Making the Bot with python

You must know:
- Python
- Telegram API
- PyTelegramBotAPI

Firstly, you must have a python installed in your system also know the basics of python. 

We have the `telegram Api key` and now we need to install the `PyTelegramBotAPI` library. To install the library use the following command.

```bash

pip install pyTelegramBotAPI

```

## Sending the first message

Now we can send the first message to the bot. To do this you need to use the `sendMessage` method of the telegram API. 

```python

import telebot # imprting the library

bot = telebot.TeleBot("your secret token") # creating the bot object

bot.send_message("your chat id", "Hello, I am Mood Fixer bot") # sending the message

```


This is would work but you need to know the `chat id` of the user. Or else there is no way to send the message to the user.


## Getting the chat id

To get the chat id you need to use the `getUpdates` method of the telegram API. This method will return the chat id of the user.

```python

import telebot # imprting the library

bot = telebot.TeleBot("your secret token") # creating the bot object

updates = bot.get_updates() # getting the updates

print(updates) # printing the updates

```

This will return the chat id of the user. Now you can use this chat id to send the message to the user.

This process is very time-consuming and also not a good way to get the chat id. So we can use the `message_handler` method of the `PyTelegramBotAPI` library.

## Using the message_handler method

```python

import telebot # imprting the library

bot = telebot.TeleBot("your secret token") # creating the bot object

@bot.message_handler(commands=['start']) # handling the start command
def send_welcome(message):
    bot.reply_to(message, "Hello, I am Mood Fixer bot")

bot.polling() # polling the bot

```

> @bot.message_handler() decorator is used to handle the messages. which returns the message to the user. We can pass the `commands` parameter to the decorator to handle the commands.

> Commands are the messages that start with the `/` symbol. For example, `/start`, `/help`, etc.

The `message_handler` method will handle the messages for every user. Now you can send the message to the user without knowing the chat id.

SOOO, now you have successfully created a bot that can send the message to the user on `/start` command. Now you can add more commands to the bot to make it more interactive.



