from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker # sessionmaker is a factory for making session objects
from sqlalchemy.ext.declarative import declarative_base # declarative_base is a factory function that constructs a base class for declarative class definitions

DATABASE_URL = "sqlite:///./bot/database/database.db"

# create an engine object
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# create a sessionmaker object
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create a base class
Base = declarative_base()

def init_db():
    import bot.database.models
    Base.metadata.create_all(bind=engine)