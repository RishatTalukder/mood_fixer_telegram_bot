from sqlalchemy import Column, Integer, String
from bot.database.db_setup import Base


class Joke(Base):
    __tablename__ = 'jokes'
    id = Column(Integer, primary_key=True, index=True)
    joke = Column(String, index=True)

class MotivationalQuote(Base):
    __tablename__ = 'motivational_quotes'
    id = Column(Integer, primary_key=True, index=True)
    quote = Column(String, index=True)


    