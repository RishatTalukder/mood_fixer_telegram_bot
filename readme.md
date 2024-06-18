# Mood Fixer Bot

This is a Telegram bot designed to fix your mood. It can respond to your mood messages with jokes or motivational quotes.

## Features

- `/start`: Start the bot and get a welcome message with instructions.
- `/mood`: Share your mood and get a response.
- `/talk`: Talk to an AI (to be implemented).

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/mood_fixer_bot.git
    cd mood_fixer_bot
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file and add your Telegram API token:
    ```sh
    TELEGRAM_API_TOKEN=your_telegram_api_token_here
    ```

5. Run the bot:
    ```sh
    python main.py
    ```

## Usage

- Start a chat with your bot on Telegram and use the `/start` command to see the available features.

## Contributing

Feel free to open issues or submit pull requests for improvements or new features.
