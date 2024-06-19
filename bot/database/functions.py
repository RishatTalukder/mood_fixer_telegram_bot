from bot.database.models import Joke, MotivationalQuote
from sqlalchemy.orm import Session
from random import choice

def create_joke(db: Session, content: str) -> Joke:
    try:
        joke = Joke(joke=content)
        db.add(joke)
        db.commit()
        db.refresh(joke)
        return joke
    except Exception as e:
        db.rollback()
        print(f"Error creating joke: {e}")
        return None

def get_jokes(db: Session):
    try:
        return db.query(Joke).all()
    except Exception as e:
        print(f"Error retrieving jokes: {e}")
        return []

def create_motivational_quote(db: Session, content: str) -> MotivationalQuote:
    try:
        quote = MotivationalQuote(quote=content)
        db.add(quote)
        db.commit()
        db.refresh(quote)
        return quote
    except Exception as e:
        db.rollback()
        print(f"Error creating motivational quote: {e}")
        return None

def get_motivational_quotes(db: Session):
    try:
        return db.query(MotivationalQuote).all()
    except Exception as e:
        print(f"Error retrieving motivational quotes: {e}")
        return []

def get_random_joke(db: Session) -> str:
    try:
        jokes = get_jokes(db)
        return choice(jokes).joke if jokes else "No jokes available."
    except Exception as e:
        print(f"Error retrieving random joke: {e}")
        return "An error occurred while fetching a joke."

def get_random_quote(db: Session) -> str:
    try:
        quotes = get_motivational_quotes(db)
        return choice(quotes).quote if quotes else "No quotes available."
    except Exception as e:
        print(f"Error retrieving random quote: {e}")
        return "An error occurred while fetching a quote."

def add_placeholders():
    """
    Adds placeholder jokes and quotes to the database.
    """
    session = SessionLocal()

    try:
        # Placeholder jokes
        jokes = [
            Joke(joke="Why don't scientists trust atoms? Because they make up everything!",),
            Joke(joke="Why was the math book sad? Because it had too many problems.",),
            Joke(joke="I told my computer I needed a break, and now it won’t stop sending me Kit-Kats!",)
        ]

        # Placeholder quotes
        quotes = [
            MotivationalQuote(quote="Believe you can and you're halfway there.",),
            MotivationalQuote(quote="You are stronger than you think.",),
            MotivationalQuote(quote="Keep pushing forward, no matter what.",)
        ]

        session.add_all(jokes)
        session.add_all(quotes)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error adding placeholders: {e}")
    finally:
        session.close()
