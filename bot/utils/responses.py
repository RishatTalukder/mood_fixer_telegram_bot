from random import choice
from bot.database.db_setup import SessionLocal
from bot.database.functions import get_random_joke, get_random_quote

def get_mood_response(mood):
    """
    This function maps moods to responses and returns an appropriate response.
    """
    try:
        session = SessionLocal()

        mood_dict = {
            'happy': get_random_quote(session),
            'sad': get_random_joke(session),
            'angry': get_random_joke(session)  # Assuming jokes for 'angry' mood
        }

        response = mood_dict.get(mood, "I am sorry! I am not trained to understand that!😊")
    except Exception as e:
        response = f"An error occurred while fetching the response: {e}"
    finally:
        session.close()

    return response
