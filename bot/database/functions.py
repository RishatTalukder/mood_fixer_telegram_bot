# bot/database/functions.py

from bot.database.models import Joke, MotivationalQuote
from sqlalchemy.orm import Session
from bot.database.db_setup import SessionLocal
from random import choice

def create_joke(db: Session, content: str) -> Joke:
    joke = Joke(joke=content)
    db.add(joke)
    db.commit()
    db.refresh(joke)
    return joke

def get_jokes(db: Session):
    return db.query(Joke).all()

def create_motivational_quote(db: Session, content: str) -> MotivationalQuote:
    quote = MotivationalQuote(quote=content)
    db.add(quote)
    db.commit()
    db.refresh(quote)
    return quote

def get_motivational_quotes(db: Session):
    return db.query(MotivationalQuote).all()

def get_random_joke(db: Session) -> str:
    jokes = get_jokes(db)
    return choice(jokes).joke if jokes else "No jokes available."

def get_random_quote(db: Session) -> str:
    quotes = get_motivational_quotes(db)
    return choice(quotes).quote if quotes else "No quotes available."

def add_placeholders():
    """
    Adds placeholder jokes and quotes to the database.
    """
    session = SessionLocal()

    # Placeholder jokes
    jokes = [
        Joke(joke="Why don't scientists trust atoms? Because they make up everything!"),
        Joke(joke="Why was the math book sad? Because it had too many problems."),
        Joke(joke="I told my computer I needed a break, and now it won’t stop sending me Kit-Kats!")
    ]

    # Placeholder quotes
    quotes = [
        MotivationalQuote(quote="Believe you can and you're halfway there."),
        MotivationalQuote(quote="You are stronger than you think."),
        MotivationalQuote(quote="Keep pushing forward, no matter what.")
    ]

    session.add_all(jokes)
    session.add_all(quotes)
    session.commit()
    session.close()

    print("Placeholders added to the database.")
